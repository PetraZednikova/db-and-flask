from flask import Flask, render_template, request
from user_list import users
import os


app = Flask(__name__)


@app.route("/")    #decorater
def domu():
    return render_template("pages/domu.html") # výstup

@app.route("/o_nas")
def o_nas():
    return render_template("pages/o_nas.html")

@app.route("/kontakty")
def kontakt():
    return render_template("pages/kontakty.html")

@app.route("/uzivatele")
def uzivatele():
    return render_template("pages/uzivatele.html", users=users)

@app.route("/detail_uzivatele/<int:id>")
def detail_uzivatele(id):
    return render_template("pages/detail_uzivatele.html", user=users[id])

@app.route("/zpravy", methods=["GET", "POST"])
def zpravy():
    if request.method == "POST":
        message = request.form["message"]
        print(message)

    return render_template("pages/zpravy.html")

if __name__=="__main__":
    app.run(debug=True)
