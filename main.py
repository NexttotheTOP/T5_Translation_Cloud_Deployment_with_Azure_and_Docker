# This file is gonna contain the routes for our webserver 

from fastapi import FastAPI, BackgroundTasks # Used to create our webserver 
from pydantic import BaseModel, validator # Used to validata data, otherwise might get errors 
import tasks

# Initializing our webapplication 

app = FastAPI()

# Defining a list of languages that our API supports 
languages = ['English', 'French', 'German', 'Romanian', 'Dutch']

class Translation(BaseModel):
    text: str
    base_lang: str
    wanted_lang: str

    # After we have made sure that all our inputs are strings, we are passing them trough our validator,
    # to make sure the data is valid/correct, ensures that our route gets proper data 
    @validator ('base_lang', 'wanted_lang') # Decorator: Adds additional value to a function 
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid language")
        return lang

## Route 1: / 
## Testing if everything is working 
## {Test message: We are live babyy! }
@app.get("/")  # Index route 
def get_root():
    return {"message": "we are live babyy!"}

## Route 2: / Translate 
## Taking in a transaltion request, and storing it to the database
## Returns a translation id 
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks): # backgroundtasks: Enables our translation to run in the background 
    t_id = tasks.store_translation(t) # Store the translation to database and gets the id of the translation 
    background_tasks.add_task(tasks.run_translation, t_id) # Runs translation in background 
    return {"task_id": t_id} # Returns translation to the user 

## Route 3: / Results 
## Taking in a translation id 
## Returning the translated text by passing in the find translation function from tasks.py and simply putting in the tasks id 
@app.get("/results")
def get_translation(t_id: int):
    return {"translation": tasks.find_translation(t_id)}

