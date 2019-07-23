# Section: importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Section: Importing data sets
dataset = pd.read_csv('Data.csv')
# x is a matrix of dependent variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Section: splitting data into training and test set
from sklearn.model_selection import train_test_split  # model_selection earlier cross_validation

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""
# Section: feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)
"""
