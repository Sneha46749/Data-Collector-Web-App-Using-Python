from flask import Flask,render_template,request

app=Flask(__name__)

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

