from flask import Flask,jsonify,request

app = Flask(__name__)

marks = [{"userID": "Naren123",
          "details": [{"name": "narendra", "Marks": 512}, ]
          }, ]

@app.route('/')
def home():
    "Home Page"
    return "Home page"

#Get marks method, This will send all user details
@app.route('/marks/',methods = ['get'])
def send_marks():
    return jsonify({"Marks": marks})

# get a specific user
@app.route('/marks/<string:userID>',methods = ['get'])
def send_userDetails(userID):
    for user in marks:
        if user["userID"] == userID:
            return jsonify({"userID": user["userID"],"details":user["details"]})
"""
Get methods can be tested directly by web browser but the testing of postmethods need specific tool ex : postman

""" 

# Create new user method
@app.route('/marks/',methods = ['post'])
def create_user():
    get_ID = request.get_json()
    new_user = {"userID":get_ID['userID'],"details":[]}
    marks.append(new_user)
    return jsonify(new_user)

# add the marks/details of a specified user
@app.route('/marks/<string:userID>/details/',methods = ['post'])
def add_details(userID):
    get_details = request.get_json()
    for user in marks:
        if user["userID"] == userID:
            details = {"name": get_details["name"]
                       ,"marks":get_details["marks"]}
            user["details"].append(details)
            return details

app.run()
