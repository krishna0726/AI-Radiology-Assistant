from radiology_assistant import app

@app.route("/")
def home():
    return "Home Page"