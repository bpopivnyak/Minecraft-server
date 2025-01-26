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


@app.route("/Minecraft_server")
def Ms():
    return render_template("MS_1.html")


@app.route("/Minecraft_server2")
def MS2():
    return render_template("MS_2.html")


@app.route("/Minecraft_server3")
def MS3():
    return render_template("MS_3.html")

@app.route("/Minecraft_server4")
def MS4():
    return render_template("MS_4.html")


@app.route("/Minecraft_server5")
def MS5():
    return render_template("MS_5.html")

@app.route("/Minecraft_server6")
def MS6():
    return render_template("MS_6.html")

@app.route("/Minecraft_server7")
def MS7():
    return render_template("MS_7.html")


@app.route("/Minecraft_server8")
def MS8():
    return render_template("MS_8.html")

@app.route("/Minecraft_server9")
def MS9():
    return render_template("MS_9.html")
app.run()

@app.route("/Minecraft_server10")
def MS10():
    return render_template("MS_10.html")
app.run()

@app.route("/Minecraft_server11")
def MS11():
    return render_template("MS_11.html")

@app.route("/Minecraft_server12")
def MS12():
    return render_template("MS_12.html")

@app.route("/Minecraft_server13")
def MS13():
    return render_template("MS_13.html")

@app.route("/Minecraft_server14")
def MS14():
    return render_template("MS_14.html")
app.run()



