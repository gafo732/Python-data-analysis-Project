from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle as p
import json
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():

    data = request.get_json()

    df = pd.DataFrame(data).T

    test_numbers = df.drop([1,14],axis=1)
    test_category = df[[1,14]]

    scaled = scaler.transform(test_numbers)
    encoded = one_hot_encoder.transform(test_category)

    final_data = np.concatenate([scaled,encoded],axis=1)
    
    result = model.predict(final_data)
    
    return jsonify(result = round(float(result),3))


if __name__ == '__main__':
    modelfile = 'model/final_model.pickle'
    model = p.load(open(modelfile, 'rb'))
    scaler = p.load(open('model/scaler.pickle', 'rb'))
    one_hot_encoder = p.load(open('model/hotencoder.pickle', 'rb'))
    app.run(debug=False, host='0.0.0.0')