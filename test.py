import pickle
import numpy as np

from flask import Flask, render_template,redirect, request

app = Flask(__name__)
model = pickle.load(open('classification.sav', 'rb'))

@app.route('/')
def main():
    red = request.l

@app.route('/predict', methods = ['POST'])
def getPredict():
    temp = request.form['temp']
    humid = request.form['humid']
    light = request.form['light']
    soil = request.form['soil']
    ec = request.form['ec']

    data = [temp,humid,light,soil,ec]

    x_test = np.array(data)
    x_test = x_test.reshape((1,-1))

    predicted = model.predict(x_test)

    return render_template("index.html.php",my_pred = predicted)

    # predicted = 1 / (1 + np.exp(-predicted))
    # return render_template('index.html',
    # prediction_text = f'Predicted: {predicted * 100:.2f}%')

if __name__ == '__main__':
    app.run(debug = True)


