import pymongo
class DatabaseConnection:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Initialize database connection here
            cls._instance.client = pymongo.MongoClient("mongodb+srv://nibhas:nibhas@cluster0.ndn704r.mongodb.net/")
        return cls._instance
    def get_client(self):
        return self.client
    

