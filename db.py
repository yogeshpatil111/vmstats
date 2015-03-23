from pymongo import MongoClient

database_url = 'mongodb://localhost:27017/test'
collection_name = "vmstats"

"""
DataBase class for data operations
"""
class DB:

    """
    Constructor : Accepts collection input for communocating with different collections in the DB.
    """
    def __init__(self,collection="vmstats"):
        self.client = MongoClient(database_url)
        self.db = self.client.get_default_database()
        if collection:
            if collection_name not in self.db.collection_names():
                self.db.create_collection(collection)
            self.col = self.db[collection]
        else:
            self.col = None

    """
    Destructor : Drop mongo connections`
    """
    def __del__(self):
        self.client.close()

    """
    Store document in the collection.
    """
    def store(self,document=[]):
        self.col.insert(document)

    """
    Retrieve data based on filter. Just return the cursor for traversal.
    """
    def retrieve(self,filter=None):
        cur = self.col.find(filter)
        return cur

    """
    Create Collection explicitly in the Database
    """
    def createCollection(self,collection="vmstats"):
        self.db.create_collection(collection)
        self.col = self.db[collection]

    """
    Drop collection from the database
    """
    def dropCollection(self,collection=None):
        if not collection:
            collection = collection_name
        if collection in self.db.collection_names():
            self.db.drop_collection(collection)
    
    
