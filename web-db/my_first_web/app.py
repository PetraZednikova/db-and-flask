from flask import Flask, render_template, request
from fake_db import users


app = Flask(__name__)


@app.route('/')    #decorater
def home():
    return render_template("pages/home.html") # výstup

@app.route('/about')
def about():
    return render_template("pages/about.html")

@app.route('/contact')
def contact():
    return render_template("pages/contact.html")

@app.route("/calc/<int:a>/<int:b>")
def calculator(a, b):
    #a = 10
    #b = 20
    return render_template("pages/calc.html", a=a, b=b, suma= a+b)

@app.route("/users")
def user_list():
    return render_template("pages/users_list.html", users=users)

@app.route("/users/<int:id>")
def user_detail(id):
    return render_template("pages/users_detail.html", user=users[id])

@app.route("/mes", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        message = request.form["message"]
        print(message)

    return render_template("/pages/chat.html")

if __name__=="__main__":
    app.run(debug=True)



