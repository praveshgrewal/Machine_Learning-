from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome "

@app.route("/index")
def index():
    return " index page"


if __name__=="__main__":
    app.run(debug=True)