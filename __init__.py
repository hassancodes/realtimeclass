from flask import Flask
from flask import render_template,redirect,request,session
import json
import requests
import os

application = Flask(__name__)
application.secret_key = "botsystematic"


dictionary = {}
@application.route("/")
def login():
    return render_template("login.html")


@application.route("/enterClass")
def enterClass():
    if "username" in session:
        return render_template("class.html", dictionary=dictionary)
    else:
        return redirect("/")


@application.route("/handlecred", methods=['POST'])
def handlecred():
    if request.method == "POST":
        studid = request.form["studentid"]
        pw = request.form["pass"]
        with open("data.json", "r") as pd:
            a = pd.read()
            rawdata = json.loads(a)
            for users in rawdata:
                if rawdata[users]["username"] == studid and rawdata[users]["password"] == pw:
                    session["username"] = studid
                    session["password"] = pw
                    return redirect("/enterClass")
            else:
                return redirect("/")


# function for sending textmessages
@application.route("/sendmessages", methods=["POST"])
def sendmessages():
    text = request.form["text"]
    print(text)
    obj = {"text": text,
    "username": session["username"],
    "secret": "iamdope"}

    req = requests.post("http://127.0.0.1:8000/chat", data=obj)
    text = req.text
    dat = json.loads(text)
    dictionary.update({dat["username"] : dat["text"]})
    print(dictionary)

    if os.path.getsize('text.json') == 0:
        with open("text.json", "r+") as file:
            json.dump(dictionary, file)

    elif os.path.getsize('text.json') != 0:
        with open("text.json", "r+") as flo:
            data = flo.read()
            print("DATA________________________",data)
            flo.seek(0)
            json.dump(data, flo)

    with open("text.json", "r") as fl:
        data = json.loads(fl.read())
        print(data)


    return redirect("/enterClass")




    # return redirect("/enterClass" , dictionary=dictionary)





@application.route("/createaccount")
def createaccount():
    return "LOL"


if __name__ == '__main__':
	application.run(debug=True)
