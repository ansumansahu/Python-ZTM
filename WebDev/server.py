from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#home page with username
def homepage(username='Me'):
    return render_template('test_index.html',name=username)

@app.route("/<username>") #not a main func(test)
#enter any random name 
def UserName(username='Me'):
    return render_template('test_index.html',name=username)

@app.route("/about")
#about me page 
def about():
    return render_template('test_about.html')

@app.route("/blog")
def blog():
    return "<p>Welcome To My Blog: To Be Updated</p>"
