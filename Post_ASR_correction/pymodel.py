from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

def load_model(MODEL_CHECKPOINT = "./google/flan-t5-small-finetuned-asr_correction"):

    tokenizer = AutoTokenizer.from_pretrained(MODEL_CHECKPOINT)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_CHECKPOINT)

    return model, tokenizer

def correct(text, model, tokenizer):
    input_ids = tokenizer(text, return_tensors="pt")["input_ids"]
    output = model.generate(input_ids)
    translated_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    return translated_text

# load_model()