from datasets import load_dataset
from transformers import AutoTokenizer
import evaluate

from main import getChatbotOutput
import numpy as np


tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad") #distilbert-base-cased-distilled-squad
dataset = load_dataset('json', data_files='train-test.json', split="train")

max_length = 384
stride = 128

def preprocess_validation_examples(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = tokenizer(
        questions,
        examples["context"],
        max_length=max_length,
        truncation="only_second",
        stride=stride,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )

    sample_map = inputs.pop("overflow_to_sample_mapping")
    example_ids = []

    for i in range(len(inputs["input_ids"])):
        sample_idx = sample_map[i]
        example_ids.append(examples["id"][sample_idx])

        sequence_ids = inputs.sequence_ids(i)
        offset = inputs["offset_mapping"][i]
        inputs["offset_mapping"][i] = [
            o if sequence_ids[k] == 1 else None for k, o in enumerate(offset)
        ]

    inputs["example_id"] = example_ids
    return inputs

validation_dataset = dataset.map(
    preprocess_validation_examples,
    batched=True,
    remove_columns=dataset.column_names
)

n_best = 20
max_answer_length = 30
predicted_answers = []

id = 0
for data in dataset:
    # append model's answer to predicted_answers
    predicted_answers.append({"id" : data["id"], "prediction_text" : getChatbotOutput(data["question"])})

metric = evaluate.load("squad")

theoretical_answers = [
    {"id": data["id"], "answers": data["answers"]} for data in dataset
]


metricCompute = metric.compute(predictions=predicted_answers, references=theoretical_answers)

print("\nExact Match %: " + str(metricCompute['exact_match']))
print("\nF1 Score %: " + str(round(metricCompute['f1'], 2)))

print(theoretical_answers)
print(predicted_answers)
