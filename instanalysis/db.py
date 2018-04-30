from flask_pymongo import PyMongo
from flask import Flask
import flask_pymongo

app = Flask(__name__)
mongo = PyMongo(app)

# I COMMENTED THIS LINE OUT BECAUSE I COULDN'T FIND OUT WHERE IT WAS IMPORTED
# FROM. IMPORT THE FUNCTION, AND THEN UNCOMMENT.
#DBQuery.shellBatchSize = 100

""" check if this user is already in the database
	return True if he/she is in the database
	return False if not
"""
def check_user(username):
	collection = mongo.db.list_collection_names()
	if username in collection:
		return True
	else:
		return False

""" get all img id for this user and return a list of it """
def get_list_of_img_id(username):
	list_img = mongo.db.username.distinct("imgID")
	return list_img

""" update database """
def update_db(username, output):
	for i in range(len(output)):
		mongo.db.username.insert({"imgID": output[i][1], "imgTime": output[i][2], "caption": output[i][3], 
			"userLiked": output[i][4], "imgLiked": output[i][5], "hashtages": output[i][6], 
			"imgFilter": output[i][7], "comment": output[i][8], "userTagged": output[i][9], 
			"gData": output[i][10]})
	#return "finish update"

""" output everything in this collection with username in front"""
def output_db(username):
	one = mongo.db.username.distinct("imgID")
	two = mongo.db.username.distinct("iimgTimemgID")
	three = mongo.db.username.distinct("caption")
	four = mongo.db.username.distinct("userLiked")
	five = mongo.db.username.distinct("imgLiked")
	six = mongo.db.username.distinct("hashtages")
	seven = mongo.db.username.distinct("imgFilter")
	eight = mongo.db.username.distinct("comment")
	nine = mongo.db.username.distinct("userTagged")
	ten = mongo.db.username.distinct("gData")
	output = []
	for i in range(len(one)):
		temp = []
		temp.append(one[i])
		temp.append(two[i])
		temp.append(three[i])
		temp.append(four[i])
		temp.append(five[i])
		temp.append(six[i])
		temp.append(seven[i])
		temp.append(eight[i])
		temp.append(nine[i])
		temp.append(ten[i])
		output.append(temp)
	return output


