import json
import numpy as np 
from keras.layers import LSTM
from keras.models import Sequential
import pandas as pd 
import matplotlib.pyplot as plt 
import nltk

data = pd.read_json('myMedChatData.json')

