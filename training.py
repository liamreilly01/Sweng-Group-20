from transformers import pipeline
import json
from datasets import load_dataset
from transformers import DefaultDataCollator
from transformers import AutoTokenizer

#Load a JSON file

dataset = load_dataset('json', data_files='train-test.json', split="train")

# dataset.shape outputs cols

print(len(dataset["train"][0]))

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def makeListFromLabel(list, label):
    newList = []
    currentList = list['train'][0]
    for i in range(len(currentList)):
        newList.append(currentList[i][label])
    return newList

def makeAnswersList(list):
    newList = []
    currentList = list['train'][0]
    for i in range(len(currentList)):
        newList.append(currentList[i]["Answers"])
    return newList

def preprocess_function(examples):
    questions = makeListFromLabel(examples, 'Question')
    context = makeListFromLabel(examples, 'Context')
    # print(examples['train'][0])
    # questions = [q.strip() for q in examples["train"][0][i]["Question"]]
    print(questions)

    inputs = tokenizer(
        questions,
        context,
        max_length=384,
        truncation="only_second",
        return_offsets_mapping=True,
        padding="max_length",
    )
    
    offset_mapping = inputs.pop("offset_mapping")
    answers = makeAnswersList(examples)
    start_positions = []
    end_positions = []
    
    for i, offset in enumerate(offset_mapping):
        answer = answers[i]
        start_char = answer["Answer_Start"][0]
        end_char = answer["Answer_Start"][0] + len(answer["Text"][0])
        sequence_ids = inputs.sequence_ids(i)
    
        # Find the start and end of the context
        idx = 0
        while sequence_ids[idx] != 1:
            idx += 1
        context_start = idx
        while sequence_ids[idx] == 1:
            idx += 1
        context_end = idx - 1
    
        # If the answer is not fully inside the context, label it (0, 0)
        if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
            start_positions.append(0)
            end_positions.append(0)
        else:
            # Otherwise it's the start and end token positions
            idx = context_start
            while idx <= context_end and offset[idx][0] <= start_char:
                idx += 1
            start_positions.append(idx - 1)
    
            idx = context_end
            while idx >= context_start and offset[idx][1] >= end_char:
                idx -= 1
            end_positions.append(idx + 1)
    
    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    return inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)
data_collator = DefaultDataCollator()

from transformers import AutoModelForQuestionAnswering, trainingArguments, trainer

model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")

training_args = trainingArguments(
    output_dir="qa_model",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=False,
)

trainer = trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

firstLoad()

try:
    trainingData = open('train-test.json', "r", encoding="utf-8")
    try:
        trainingDataDictionary = json.loads(trainingData.read())
    except:
        print("ERROR loading and reading Sample_Acts.json")
    finally:
        trainingData.close()
except:
    print("ERROR opening Sample_Acts.json")

def firstLoad():
    model = pipeline(model='distilbert-base-cased-distilled-squad')
    model.save_pretrained('./model/')