from peewee import Model, SqliteDatabase, CharField, TextField

# Initializing our databse 

db = SqliteDatabase('translations.db')

# Defining a class -> a databse tabel and the columns 

class TranslationModel(Model):
    text = TextField() # Text they want to translate 
    base_lang = CharField() # Language they want to translate from
    wanted_lang = CharField() # Language they want to translate to 
    translation = TextField(null=True)

# Using the database to store the model 

    class Meta:
        database = db

# Creates our table if it doesn't exist yet 

db.create_tables([TranslationModel])

''' What all this code is doing is finding a way for us to 
interact with and creating a Sqlite database for us to store our data in ''' 