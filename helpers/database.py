import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

# Now you can access the list of databases
db=client.news
print(db)

def save_data_to_db(collection_name,data):
    try:
        collection=db[collection_name]
        return collection.insert_one(data).inserted_id

    except Exception as e:
        return None

def get_data_from_db(collection_name,data):
    try:
        # Collection=db[collection_name]
        # print(db.Collection.find_one(data))
        collection=db[collection_name]
        response=collection.find_one(data)
        # for i in response:
        #     print(i)
        print(response)
        return response

    except Exception as e:
        print(e)
        return None

def update_or_create_data(collection_name,data,data_to_search):
    try:
        response=get_data_from_db(collection_name,data_to_search)
        if response is None:
            return save_data_to_db(collection_name,data)
        collection=db[collection_name]
        response=collection.update_one(data_to_search,{'$set':data})
        print( "update",response)
        return response
    except Exception as e:
        print(e)
        return None


    
