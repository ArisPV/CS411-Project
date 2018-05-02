from pymongo import MongoClient
#client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.users






# from flask_pymongo import PyMongo
# from flask import Flask
# import flask_pymongo

# app = Flask(__name__)
# app.config.from_object('config')
# mongo = PyMongo(app)


#DBQuery.shellBatchSize = 100

""" check if this user is already in the database
    return True if he/she is in the database
    return False if not
"""
def is_user_in_database(username):
    collections = mongo.db.list_collection_names()
    if username in collections:
        return True
    else:
        return False

""" get all img id for this user and return a list of it """
def get_list_of_img_ids_for(username):
    userdb = db[username]
    findings = userdb.find({})
    findingsList = list(findings) #this is a list of dictionaries
    res = []
    for finding in findingsList:
        finding = list(finding.values())
        res += [finding[1]]

    return res

""" update database """
def insert_data_for_user(username, imageData):
        #print("imageData = ",imageData)
        #print("idata 10 = ",imageData[10])

        userdb = db[username]
        userdb.insert_one(   

            {
            "imgID": imageData[1], 
            "imgTime": imageData[2], 
            "likes":imageData[5],
            "hashtages": imageData[6],
            "gData": imageData[10]
            }          

            )
    #return "finish update"

""" output everything in this collection with username in front"""
def get_use_data(username):
    userdb = db[username]
    findings = userdb.find({})
    findingsList = list(findings) #this is a list of dictionaries
    res = []
    for finding in findingsList:
        finding = list(finding.values())
        finding = finding[1:]
        res += [finding]
    #print("res =" ,res)

    return res #returns 2d lisr of all image data, one list per image


def doDBTests():
    # testnameVariable = "testnameValue"
    # print(type(mongo))# <class 'flask_pymongo.PyMongo'>
    # print(type(mongo.db)) #<class 'flask_pymongo.wrappers.Database'>
    # print(type(mongo.db.testnameVariable))
    pass
