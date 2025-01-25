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

@app.route("/Clan-page-1")
def clanInfo1():
    return render_template("Cl@n-page#1.html")

@app.route("/Clan-page-2")
def clanInfo2():
    return render_template("Cl@n-page#2.html")

@app.route("/Clan-page-3")
def clanInfo3():
    return render_template("Cl@n-page#3.html")

@app.route("/Clan-page-4")
def clanInfo4():
    return render_template("Cl@n-page#4.html")

@app.route("/Clan-page-5")
def clanInfo5():
    return render_template("Cl@n-page#5.html")

@app.route("/Clan-page-6")
def clanInfo6():
    return render_template("Cl@n-page#6.html")

@app.route("/Clan-page-7")
def clanInfo7():
    return render_template("Cl@n-page#7.html")

@app.route("/Clan-page-8")
def clanInfo8():
    return render_template("Cl@n-page#8.html")

@app.route("/Clan-page-9")
def clanInfo9():
    return render_template("Cl@n-page#9.html")
app.run()

