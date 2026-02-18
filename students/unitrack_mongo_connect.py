from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# connect to database
db = client["unitrack"]

# connect to collection
collection = db["students"]

print("Connected to MongoDB")

# count records
count = collection.count_documents({})
print("Total records:", count)

# show records
print("\nStudent Records:")

for student in collection.find():
    print(student)

