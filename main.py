
from flask import Flask, request, render_template, redirect, url_for
from flask_compress import Compress
import sqlite3

app = Flask(__name__)
Compress(app)

@app.route('/')
def aa():
    return render_template("home.html")

@app.route('/trynow',methods =["GET", "POST"])
def a():
    return render_template('trynow.html')

@app.route('/submit')
def ab():
    return render_template("modeloutput.html")

@app.route('/add')
def abc():
    return render_template("output.html")

if __name__=='__main__':
    app.run(port = 5001)
