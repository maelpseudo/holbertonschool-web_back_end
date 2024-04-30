from pymongo import MongoClient

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    :param mongo_collection: pymongo collection object
    :return: List of documents, or an empty list if no document is found
    """
    # Use the find() method to get all documents in the collection
    documents = list(mongo_collection.find())
    
    # Return the list of documents
    return documents

if __name__ == "__main__":
    # Establish connection to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specified database and collection
    school_collection = client.my_db.school
    
    # Call the function to list all documents
    schools = list_all(school_collection)
    
    # Print each document's ID and name
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
