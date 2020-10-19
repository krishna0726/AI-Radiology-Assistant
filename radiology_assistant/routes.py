from radiology_assistant import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    return "Search Results Page"

@app.route("/report")
def report():
    return render_template("report.html")