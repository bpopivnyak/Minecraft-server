from flask import *

app = Flask("The War Of World")
app.secret_key = "28800"

@app.route("/")
def Main():
    return render_template("index.html")

@app.route("/Donation")
def DonatePage():
    return render_template("Donation-shop.html")

@app.route("/Servers")
def ServerList():
    return render_template("Servers.html")

@app.route("/Cl@N$")
def Active_clans():
    return render_template("Clans.html")

@app.route("/ABOUT_US")
def Credits():
    return render_template("about_us.html")

@app.route("/Login")
def DataPlayer():
    return render_template("Login.html")


app.run()

