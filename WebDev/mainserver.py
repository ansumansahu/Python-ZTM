from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#home page
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)