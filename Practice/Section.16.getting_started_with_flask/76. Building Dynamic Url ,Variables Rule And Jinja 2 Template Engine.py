# build url dynamically
#variables rule
#jinja2 template engine

#jinja2 is a template engine for python
'''
{{ }} expression to print output in html.
{%..%}condition statment
{#} this is for comment

'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome</h1></html>"

@app.route("/about")
def start_page():
    return render_template("about.html")

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

# @app.route("/form",methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['username']
#         return f" hii ! <h1>{name}</h1>"
#     return render_template("form.html")



@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['username']
        return f" hii ! <h1>{name}</h1>"
    return render_template("form.html")

#VARIUABLES RULE

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="fail"
    expp= {'score':score,'res':res}
    return render_template('result.html',result=expp)


@app.route('/prac/<int:score>')
def prac(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="fail"
    exp= {'score':score,'res':res}
    return render_template('pro.html',result=exp)
        
#if condition
@app.route('/jiger/<int:score>')
def jiger(score):
   
  
 return render_template('result.html',result=score)

@app.route('/fail/<int:score>')
def fail(score):
   
  
 return render_template('result.html',result=score)

@app.route('/kumar',methods=['POST','GET'])
def kumar():
    total_score=0
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.form['Maths'])
        english=float(request.form['English'])
        total_score=(science+maths+english)
    else:
        return render_template('getresult.html')

    
    return redirect(url_for('prac',score=total_score)) 
   
     
   
  
 


        

if __name__=="__main__":
    app.run(debug=True)


