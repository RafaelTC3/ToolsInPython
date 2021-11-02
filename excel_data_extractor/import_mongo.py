import json
from pymongo import MongoClient
from .config import MongoDb


def insert_data(json_file_path):
    print("create connection string")

    user = MongoDb["username"]
    password = MongoDb["password"]

    client = MongoClient(MongoDb["connection"].format(user, password))
    db = client[MongoDb["database"]]
    collection_currency = db[MongoDb["collection"]]

    print("insert json file on mongodb")

    with open(json_file_path) as f:
        file_data = json.load(f)

    if collection_currency.count() > 0:
        collection_currency.drop()

    collection_currency.insert_many(file_data)

    client.close()

    print("end of process")


def update_data():
    print("create connection string")

    user = MongoDb["username"]
    password = MongoDb["password"]

    client = MongoClient(MongoDb["connection"].format(user, password))
    db = client[MongoDb["database"]]
    collection_currency = db[MongoDb["collection"]]

    print("insert field name to be updated")
    field_name = input()
    print("insert field comparator (gt - greater than, lt - less than, eq - equal)")
    comparator = input()
    print("insert field value to be updated")
    field_value = input()
    print("insert field name to be upgraded/inserted")
    update_name = input()
    print("insert field value to be upgraded/inserted")
    update_value = input()
    print("overwrite documents? (yes/no)")
    upsert_value = input()

    if upsert_value == 'yes':
        upsert_value = False
    else:
        upsert_value = True

    query = {f"{field_name}": {f"${comparator}": f"{field_value}"}}
    update = {"$set": {update_name: update_value}}
    upsert = {"upsert": str(upsert_value).lower()}
    print(f"In case of error, insert the following query in database:\n"
          f"db.{collection_currency.name}.updateMany(\n\t{query},\n\t{update},\n\t{upsert}\n);")

    collection_currency.update_many(query, update, upsert_value)

    client.close()
