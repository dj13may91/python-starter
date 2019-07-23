# simple_linear_regression

# Section: importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Section: Importing data sets
dataset = pd.read_csv('Salary_Data.csv')
# x is a matrix (30*1) )of independent variables, here experience
X = dataset.iloc[:, :-1].values
# y is a vector here of dependent variables (as salary depends on experience)
y = dataset.iloc[:, 1].values

# Section: splitting data into training and test set
from sklearn.model_selection import train_test_split  # model_selection earlier cross_validation

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=(1 / 3), random_state=0)

"""
# Section: feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)
"""

#  Fitting simple_linear_regression to the training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the test set values
# y_pred is a vector of predicted values
y_pred = regressor.predict(x_test)

# visualizing the training set results
# plotting a line of training data in blue with actual training points in red
# here scatter is like marking all points (x[i], y[i])
plt.scatter(x_train, y_train, c='red')
plt.plot(x_train, regressor.predict(x_train), c='blue')
plt.title('salary vs experience (Training set)')
plt.xlabel('Years of exp')
plt.ylabel('Salary')
plt.show()

# visualizing the test set results
# plotting a line of training data in blue with test points in red
plt.scatter(x_test, y_test, c='red')
plt.plot(x_train, regressor.predict(x_train), c='blue')
plt.title('salary vs experience (Test set)')
plt.xlabel('Years of exp')
plt.ylabel('Salary')
plt.show()
