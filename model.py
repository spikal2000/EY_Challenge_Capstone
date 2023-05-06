# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:30:57 2023

@author: spika
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("new_crop_data.csv")
crop_data = pd.read_csv("Crop_Yield_Data_challenge_2.csv")

X = data
y = crop_data['Rice Yield (kg/ha)']

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=21)

def ExtraTreesR(X_train, y_train, n_estimators=100, max_depth=None, min_samples_split=2,max_features='auto',
                bootstrap=False):
    regressor = ExtraTreesRegressor(n_estimators=n_estimators, 
                                    max_depth=max_depth,
                                    min_samples_split=min_samples_split,
                                    max_features=max_features,
                                    bootstrap=bootstrap
                                    )
    regressor.fit(X_train, y_train)
    #model Evaluation
    print("============ExtraTreesRegressor============")
    #In sample evaluation
    insample_predictions = regressor.predict(X_train)
    print("Insample R2 Score: {0:.2f}".format(r2_score(y_train,insample_predictions)))

    #Out-sample evaluation
    outsample_predictions = regressor.predict(X_test)
    print("Outsample R2 Score: {0:.2f}".format(r2_score(y_test,outsample_predictions)))
    return regressor

"""
# Use the ExtraTreesRegressor
model = ExtraTreesR(X_train, y_train, 
                    n_estimators=110, 
                    max_depth=5, 
                    min_samples_split=10,max_features='auto',
               bootstrap=True)

new_data = X_test[:1]
y_new = y_test[:1]
predctions = model.predict(new_data)

print("Actual:", y_new, "Predicted:", predctions)
"""

