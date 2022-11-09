# Checking different libraries
import numpy as np
import pandas as pd
import string
import re
#import keras

from sklearn.model_selection import train_test_split
#from keras.models import Model


#arr = np.ones( (3,5))
print ("Hello world")
#print (arr)

# ******************** Sorting data
import operator
x = { 1:[ 'a', 7], 4:['b',  13], 2:['c', 11]}
sorted_x = sorted( x.items(), key=operator.itemgetter(1), reverse = True )
print (sorted_x)

# ******************** Storing data
import pickle
import csv


import copy
import time
import datetime
import random

print ( random.randint( 1, 10 )) # number from 1 to 10, endpoints included

# ******************** Ploting data
#import matplotlib.pyplot as plt


#import torch

print ("hello world")
my_variable = 4500
print (my_variable)

