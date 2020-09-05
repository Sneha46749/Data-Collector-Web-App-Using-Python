from flask import Flask,render_template,request
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)

"""Connectng the database with the app"""
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'  

"""Creating a class alchemy object for this falsk application"""
db = SQLAlchemy()  

class Data(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),unique=True)
    height = db.Column(db.Integer)

"""Initialising the class variables/instance variables. __init__ is the first method
 to be called when calling a class"""
def __init__(self,email,height):
    self.email = email
    self.height = height


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])   #POST is the second input that is entered by user
def success():
    if request.method=='POST':
        email = request.form["email_name"]
        height = request.form["height"]
        print(email,height)
        return render_template("success.html")    

if __name__ == "__main__":
    app.debug=True
    app.run() 

