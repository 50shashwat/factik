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

print("Output from Python") 

#this is the model file pickle_file_name.pkl
fname = 'pickle_file_name.pkl'
#loading the model
model = joblib.load(open(fname, 'rb'))

#bag of words file opening the file and loading it
infil = open("feature.pkl",'rb')
new_bow = pickle.load(infil)
infil.close()

#this is the inout against which we are testing
input = ['Trump said hundreds  of governors are calling him & we only have 50']
print(input)

#converting the string to numbers using bag of words
aah = new_bow.transform(input).toarray()

var = model.predict(aah)
print('first step')
# 0 means false 1 means true just binary classification
print(var)

# getting the percentage at 0 index is fake percentage and 1 index is True 
print('second step')

from sklearn.metrics import log_loss
probs = model.predict_proba(aah)
print('fake percentage ', probs[:,0]*100)
print('True Percentage ', probs[:,1]*100)



 
