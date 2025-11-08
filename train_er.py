import json
import numpy as np
from datasets import load_dataset
from transformers import (
    AutoTokenizer, 
    AutoModelForTokenClassification, 
    DataCollatorForTokenClassification, 
    TrainingArguments, 
    Trainer
)
from seqeval.metrics import f1_score, classification_report

MODEL_NAME = "distilbert-base-uncased"
MAX_LEN = 128

# Load label mappings
with open("labels.json") as f:
    labels = json.load(f)["labels"]
label2id = {l:i for i,l in enumerate(labels)}
id2label = {i:l for i,l in enumerate(labels)}

# Load dataset
data_files = {
    "train": "data/train.jsonl",
    "validation": "data/dev.jsonl",
    "test": "data/test.jsonl"
}
raw_datasets = load_dataset("json", data_files=data_files)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)

def tokenize_and_align(examples):
    encodings = tokenizer(examples["text"], truncation=True, max_length=MAX_LEN, return_offsets_mapping=True)
    all_labels = []
    for text, entities, offsets in zip(examples["text"], examples["entities"], encodings["offset_mapping"]):
        char_labels = ["O"] * len(text)
        for e in entities:
            s, e_, lab = e["start"], e["end"], e["label"]
            char_labels[s] = "B-" + lab
            for i in range(s + 1, e_):
                if char_labels[i] == "O":
                    char_labels[i] = "I-" + lab
        label_ids = []
        for s, e_ in offsets:
            if s == e_:
                label_ids.append(-100)
            else:
                span = char_labels[s:e_]
                tag = "O"
                if any(t.startswith("B-") for t in span):
                    tag = next(t for t in span if t.startswith("B-"))
                elif any(t.startswith("I-") for t in span):
                    tag = next(t for t in span if t.startswith("I-"))
                label_ids.append(label2id[tag])
        all_labels.append(label_ids)
    encodings["labels"] = all_labels
    encodings.pop("offset_mapping")
    return encodings

tokenized = raw_datasets.map(tokenize_and_align, batched=True, remove_columns=raw_datasets["train"].column_names)
data_collator = DataCollatorForTokenClassification(tokenizer)

model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME, num_labels=len(labels), id2label=id2label, label2id=label2id)

def compute_metrics(p):
    preds = np.argmax(p.predictions, axis=-1)
    labels_arr = p.label_ids
    pred_tags, true_tags = [], []
    for p_seq, t_seq in zip(preds, labels_arr):
        p_tags, t_tags = [], []
        for p_id, t_id in zip(p_seq, t_seq):
            if t_id == -100: continue
            p_tags.append(id2label[p_id]); t_tags.append(id2label[t_id])
        pred_tags.append(p_tags); true_tags.append(t_tags)
    return {"f1": f1_score(true_tags, pred_tags)}

args = TrainingArguments(
    output_dir="backend/model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=5e-5,
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

trainer.train()
trainer.save_model("backend/model")
tokenizer.save_pretrained("backend/model")

pred = trainer.predict(tokenized["test"])
print(pred.metrics)
