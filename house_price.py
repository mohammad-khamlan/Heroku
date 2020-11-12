from flask import Flask, request, jsonify
import pickle
import sklearn
import numpy as np
from argparse import ArgumentParser
import os

app = Flask(__name__)


def loaded_model():
    """
    loaded the model using path passed in the console
    :param: none
    :return: the model loaded from pickle file
    """
    #Loaded model by pickle packege
    with open(str(path), 'rb') as f:
        model = pickle.load(f)
    return model



@app.route('/', methods=['GET', 'POST'])
def predict():
    """
    predict the house price by using the model
    :param: none
    :return: house price prediction
    """

    features = []

    if request.method == 'POST':
        #get features from json request
        req_json = request.json
        
        features.append(req_json['date'])
        features.append(req_json['house_age'])
        features.append(req_json['station_distance'])
        features.append(req_json['stores'])
        features.append(req_json['latitude'])
        features.append(req_json['longitude'])
        
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = str(model.predict(features))
        #return the result of the model
        return jsonify(result)

        
    else:
        #get features from get url
        
        features = request.args.get("date")
        features = request.args.get("house_age")
        features = request.args.get("station_distance")
        features = request.args.get("stores")
        features = request.args.get("latitude")
        features = request.args.get("longitude")
        
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = model.predict(features)
        #return the result of the model
        return str(result)    


if __name__ == '__main__':
    #Pass argument (path) from terminal
    parser = ArgumentParser()
    parser.add_argument('-p')
    args = parser.parse_args()
    path = args.p
    #Loaded model
    model = loaded_model() 
    #Run flask application
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=False,host='0.0.0.0', port =port)
