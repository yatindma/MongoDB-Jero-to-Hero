from pymongo import MongoClient

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Define the collections
collection_one = db["Learn1"]
collection_two = db["Learn2"]

# Insert dummy data into Learn1 collection
post_1 = {"commonField": 1, "name": "John", "age": 28}
post_2 = {"commonField": 2, "name": "Yatin", "age": 32}
post_3 = {"commonField": 3, "name": "Mark", "age": 25}
post_4 = {"commonField": 4, "name": "Tom", "age": 40}
collection_one.insert_many([post_1, post_2, post_3, post_4])

# Insert dummy data into Learn2 collection
post_5 = {"commonField": 1, "city": "New York", "state": "NY"}
post_6 = {"commonField": 2, "city": "Los Angeles", "state": "CA"}
post_7 = {"commonField": 3, "city": "San Francisco", "state": "CA"}
collection_two.insert_many([post_5, post_6, post_7])

# Perform inner join
result_inner = collection_one.aggregate([
    {
        "$lookup": {
            "from": "Learn2",
            "localField": "commonField",
            "foreignField": "commonField",
            "as": "joinedData"
        }
    },
    {
        "$unwind": "$joinedData"
    }
])
print("Inner join result:")
for r in result_inner:
    print(r)

# Perform left outer join
result_left_outer = collection_one.aggregate([
    {
        "$lookup": {
            "from": "Learn2",
            "localField": "commonField",
            "foreignField": "commonField",
            "as": "joinedData"
        }
    }
])
print("Left outer join result:")
for r in result_left_outer:
    print(r)

# Perform right outer join
result_right_outer = collection_two.aggregate([
    {
        "$lookup": {
            "from": "Learn1",
            "localField": "commonField",
            "foreignField": "commonField",
            "as": "joinedData"
        }
    }
])
print("Right outer join result:")
for r in result_right_outer:
    print(r)

# Perform full outer join
result_full_outer = collection_one.aggregate([
    {
        "$lookup": {
            "from": "Learn2",
            "localField": "commonField",
            "foreignField": "commonField",
            "as": "joinedData"
        }
    },
    {
        "$set": {
            "leftTable": "Learn1"
        }
    }
])
result_full_outer = result_full_outer + collection_two.aggregate([
    {
        "$lookup": {
            "from": "Learn1",
            "localField": "commonField",
            "foreignField": "commonField",
            "as": "joinedData"
        }
    },
    {
        "$set": {
            "leftTable": "Learn2"
        }
    }
])
print("Full outer join result:")
for r in result_full_outer:
    print(r)
