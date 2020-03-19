import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)
modelo = pickle.load(open('../scripts/modelo.pkl','rb'))

@app.route("/")
def api_online():
    return "API: Iris Online v1.0", 200

@app.route("/predict", methods = ['POST'])
def predict():
    data = request.get_json(force=True)
    predict = modelo.predict(np.array([list(data.values())]))
    output = int(predict[0])
    if(output == 0):
        output = 'Setosa'
    elif(output == 1):
        output = 'Versicolor'
    else:
        output = 'Virginica'

    response = {"Species": output}
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)