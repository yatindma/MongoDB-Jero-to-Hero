from pymongo import MongoClient

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]  # Connect to the database

# Check the database names and collection names
print("Database names:", client.list_database_names())
print("Collection names:", db.list_collection_names())

# Connect to the collection
collection = db["Learn"]

# Insert documents
post_1 = {"name": "John", "address": "Highway 37"}
post_2 = {"name": "Yatin", "address": "Highway 37"}
post_3 = {"name": "John"}
collection.insert_one(post_1)
collection.insert_many([post_2, post_3])

# Find a document which is first in the collection
print("First document in collection:", collection.find_one())

# Find a document with the name "John"
print("Document with name John:", collection.find_one({"name": "John"}))

# Print all documents in the collection with the name "Yatin"
print("Documents with name Yatin:", list(collection.find({"name": "Yatin"})))

# Print all documents in the collection which starts with the letter "J"
print("Documents starting with J:", list(collection.find({"name": {"$regex": "^J"}})))

# Print all documents in the collection which starts with the letter "J" or "j"
result = collection.find({"name": {"$regex": "^[Jj]"}})


# Print all documents in the collection which ends with the letter "n"
print("Documents ending with n:", list(collection.find({"name": {"$regex": "n$"}})))

# Count the number of documents in the collection
print("Number of documents in collection:", collection.count_documents({}))

# Count the number of documents in the collection with the name "John"
print("Number of documents with name John:", collection.count_documents({"name": "John"}))

# Sort the documents based on the name in ascending order
print("Documents sorted by name in ascending order:", list(collection.find().sort("name", 1)))
# for descending order use -1

# Delete the document with the name start with J only one document will be deleted
collection.delete_one({"name": {"$regex": "^J"}})

# Delete all documents with the name start with J
collection.delete_many({"name": {"$regex": "^J"}})

# Update the document whose name starts with J to Yatin\
collection.update_one({"name": {"$regex": "^J"}}, {"$set": {"name": "Yatin"}})

# Update all documents whose name starts with J to Yatin
collection.update_many({"name": {"$regex": "^J"}}, {"$set": {"name": "Yatin"}})

# Print all the data in the collection
print("All documents in collection:", list(collection.find()))

# add rules to the collection
phone_number_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["phone_number"],  # required field
        "properties": {
            "phone_number": {
                "bsonType": "string",
                "description": "Phone number of the user",
                "pattern": "^[0-9]{10}$"  # pattern to match the phone number format 10 digits
            }
        }
    }
}

collection = db["Learn1"]
collection.createCollection(validationLevel="strict", validator=phone_number_schema)

# Insert a document with the phone number
post_1 = {"name": "John", "address": "Highway 37", "phone_number": "123456789"}
collection.insert_one(post_1)

# Drop the collection
collection.drop()

# X-X-X-X-X-X-X-X-X-X-X- Finish X-X-X-X-X-X-X-X-X-X-X-
