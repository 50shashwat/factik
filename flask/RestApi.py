import flask
import sys 
import pickle
import joblib
import pandas as pd
from sklearn.utils import shuffle
import random
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import string
import numpy as np
import re
import nltk
import pickle
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer 
from flask import request, jsonify
from sklearn.metrics import log_loss
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getPrediction/', methods=['GET'])
def home():
	print("Output from Python") 
	fname = 'pickle_file_name.pkl'
	model = joblib.load(open(fname, 'rb'))

	infil = open("feature.pkl",'rb')
	new_bow = pickle.load(infil)
	infil.close()
	if 'inputtext' in request.args:
		id = request.args['inputtext']
	else:
		return "Error: No id field provided. Please specify an input text."
	input = [id]
	aah = new_bow.transform(input).toarray()
	var = model.predict(aah)

	probs = model.predict_proba(aah)
	x = probs[:,0]
	y = probs[:,1]
	x = x.tolist()
	y = y.tolist()
	books = [
    	{'id': 'Fake Percentage',
     	'Percentage': x },
    	{'id': 'True Percentage',
    	'Percentage': y}
	]
	return jsonify(books)

app.run(host='0.0.0.0')
