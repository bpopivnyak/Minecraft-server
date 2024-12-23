from flask import *

app = Flask("The War Of World")
app.secret_key = "28800"

@app.route("/")
def Servers():
    return render_template("index.html")

app.run()

