from asyncore import write
import email
from email import message
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/")
#home page
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

def write_to_txt(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open("./database.txt", mode = 'a') as database:
		text = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open("./database.csv", mode = 'a', newline='') as database2:
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict() #grabs data submitted as a dictionary
        write_to_txt(data)
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return 'ERROORRR!!'