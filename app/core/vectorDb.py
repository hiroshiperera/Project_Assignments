from pymilvus import connections, Collection, MilvusException, db, utility

class SetVectorDb:
    def __init__(self, reset=True):
        conn = connections.connect(host="127.0.0.1", port=19530)
        self.db_name = "milvus_demo"
        self.reset=reset        
        return self.generate_db()
        

    def generate_db(self):
        try:
            existing_databases = db.list_database()
            if self.db_name in existing_databases:
                print(f"Database '{self.db_name}' already exists.")

                if self.reset:
                    db.using_database(self.db_name)
                    collections = utility.list_collections()
                    for collection_name in collections:
                        collection = Collection(name=collection_name)
                        collection.drop()
                        print(f"Collection '{collection_name}' dropped.")

                    db.drop_database(self.db_name)
                    print(f"Database '{self.db_name}' deleted.")
                    db.create_database(self.db_name)
                    print(f"Database '{self.db_name}' created.")
                else:
                    db.using_database(self.db_name)
            else:
                db.create_database(self.db_name)
                print(f"Database '{self.db_name}' created.")
        except MilvusException as e:
            print(f"An error occurred: {e}")



