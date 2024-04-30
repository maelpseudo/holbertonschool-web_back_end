from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    :param mongo_collection: pymongo collection object
    :param topic: string, the topic searched
    :return: List of schools that have the specific topic
    """
    # Use the find method with a query that checks if the topic is in the topics array
    schools = list(mongo_collection.find({"topics": {"$in": [topic]}}))
    
    # Return the list of schools
    return schools

if __name__ == "__main__":
    # Establish connection to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # Assume that documents are already inserted as shown in the example
    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
