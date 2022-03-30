from urllib import request
from flask import Flask , render_template , request

import md as m

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ["GET","POST"])
def getPredict():
    if request.method == "POST":
        temp = request.form["temp"]
        humid = request.form["humid"]
        light = request.form["light"]
        soil = request.form["soil"]
        ec = request.form["ec"]

        prediction = m.md_prediction(temp,humid,light,soil,ec)
        # prediction = m.md_prediction(temp)
        mp = prediction[0]
        test = prediction[1]

    return render_template("index.html",my_pred = mp,t = test)

if __name__ == "__main__":
    app.run(debug=True)

