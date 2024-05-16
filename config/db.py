from pymongo import MongoClient
MONGO_URI = 'mongodb+srv://Fast_api:Fastapi11@cluster0.twzmfju.mongodb.net/'

client = MongoClient(MONGO_URI)


# Notes = client['notes']
# Notes_collection = Notes['notes']