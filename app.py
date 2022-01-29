from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/enterClass")
def enterClass():
    return render_template("class.html")




app.run(debug=True)
