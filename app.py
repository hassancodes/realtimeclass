from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")



app.run(debug=True)