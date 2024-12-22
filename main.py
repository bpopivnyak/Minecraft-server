from flask import *

app = Flask("The War Of World")
app.secret_key = "28800"

@app.route("/")
def Servers():
    return render_template("base.html")

app.run()

