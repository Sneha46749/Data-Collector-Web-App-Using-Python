from flask import Flask,render_template,request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'  
db = SQLAlchemy()  

class Data(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),unique=True)
    height = db.Column(db.Integer)

def __init__(self,email,height):
    self.email = email
    self.height = height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])   
def success():
    if request.method=='POST':
        email = request.form["email_name"]
        height = request.form["height"]
        send_email(email,height)
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data=Data(email,height)  #Creating instance of the class Data
            db.session.add(email,height)
            db.session.commit(data)  #Session class
            return render_template("success.html")    
    return render_template('index.html', 
    text = "Seems like we have got something from that email address already")

if __name__ == "__main__":
    app.debug=True
    app.run() 