# Section: importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Section: Importing data sets
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values  # -1 => we take all columns except last one
y = dataset.iloc[:, 3].values  # only 3rd column index

# Section: Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# axis = 0, means we take mean (or use 'median')  and fill the missing value
# from index 1 to 2 (3 here as upper bound is excluded)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
# above code replaces missing data in the data set


# Section:Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# anything that can be grouped in terms of values is categorical column (finite possibilities of value)
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])  # here 0 is the index of categorical column
# above assigns numeric codes to countries starting from 0 and upto n
# problem with this is that for example spain = 0 and france =1, ML will treat france > spain as 1>0
# to avoid this, we will be using OneHotEncoder class

ohEncoder = OneHotEncoder(categorical_features=[0])  # here 0 is the index of categorical column
X = ohEncoder.fit_transform(X).toarray()
# what OneHotEncoder does is that it create n columns for n different categories
# where value = 1 for category and rest all are 0

labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)

# Section: splitting data into training and test set
from sklearn.model_selection import train_test_split  # model_selection earlier cross_validation

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Section: feature scaling
from sklearn.preprocessing import StandardScaler

# we need feature scaling as in graph of x-y , if x is age and y is salary,
# then euclidean distance will be dominated by salary. So we do feature scaling in which
# we put all values in a certain range, say [-n to +n].
# Note: Some libraries do feature scaling for the model, some dont.

sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)

# Right now we dont need to scale Y as it is in same range.
# Later if there are too many values, we might need feature scaling
