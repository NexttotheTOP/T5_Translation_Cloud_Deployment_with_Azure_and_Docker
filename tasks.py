from Model import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration # Tokenizers turns our text into numbers that our DL model can process, and the conditional generation translates the tokens/numbers into our wanted language

# Downloading the Tokenizer and Generator
tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=512)
translator = T5ForConditionalGeneration.from_pretrained("t5-small")

## Store translation
## Translation request and stores/saves it to the database
def store_translation(t):
    model = TranslationModel(text=t.text, base_lang=t.base_lang, wanted_lang=t.wanted_lang)
    model.save()
    return model.id # We are using the model's id to reference to a specific translation request later and run the translation 

## Run translation
## Running a pretrained deep learning model -> runs a full translation and persists it to our database 
def run_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id) # Each translation request gets a different id 

    prefix = f"translate {model.base_lang} to {model.wanted_lang}: {model.text}" # Generates a string with the full translation of the request 
    input_ids = tokenizer(prefix, return_tensors="pt").input_ids # Splits up the sentence into tokens/"words" en turns it into numbers

    outputs = translator.generate(input_ids, max_new_tokens=512) # Generating output based on input 
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True) # Decoding the output numbers back in words/chracters
    model.translation = translation
    model.save()

## Finding the translation 
## Retrieve a translation from the databse 
def find_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id)

    translation = model.translation
    if translation is None:
        translation = "Still processing, chech again in a minute"
    return translation 