import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, model_selection

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

HousingData = pd.read_pickle('15-Data/LabeledDataset.pickle')

# X = Features
X = np.array(HousingData.drop(['Future HPI USA', 'Label'], 1))
# Convert data to values between -1 and +1
X = preprocessing.scale(X)

# y = Labels
y = np.array(HousingData['Label'])

# Configuring model
# Order of values is important!
# X values before y values
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = svm.SVC(kernel='linear')

# Training model
clf.fit(X_train, y_train)

# Testing model
result = clf.score(X_test, y_test)

print(result)