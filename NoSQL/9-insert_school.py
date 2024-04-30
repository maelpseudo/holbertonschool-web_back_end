from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.

    :param mongo_collection: pymongo collection object
    :param kwargs: Keyword arguments that define the document to insert
    :return: The new _id of the inserted document
    """
    # Insert the document defined by kwargs into the collection
    result = mongo_collection.insert_one(kwargs)

    # Return the ObjectId of the new document
    return result.inserted_id

if __name__ == "__main__":
    # Establish connection to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the specified database and collection
    school_collection = client.my_db.school

    # Insert a new school into the collection
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    # Import the function to list all documents for verification
    list_all = __import__('8-all').list_all

    # List all schools to see the newly added school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
