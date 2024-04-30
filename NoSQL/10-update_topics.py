from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the school name.

    :param mongo_collection: pymongo collection object
    :param name: string, the school name to update
    :param topics: list of strings, the list of topics approached in the school
    """
    # Update the document where name matches the provided name
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

if __name__ == "__main__":
    # Establish connection to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    
    # Update topics for a specific school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Function to list all schools to see the updated topics
    list_all = __import__('8-all').list_all
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # Update topics again to show different input and output
    update_topics(school_collection, "Holberton school", ["iOS"])
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
