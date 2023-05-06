# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:30:57 2023

@author: spika
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor

data = pd.read_csv("new_crop_data.csv")
crop_data = pd.read_csv("Crop_Yield_Data_challenge_2.csv")

X = data
y = crop_data['Rice Yield (kg/ha)']

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=21)

#Model Training
regressor = ExtraTreesRegressor(bootstrap=False, ccp_alpha=0.0, criterion='mse',
                    max_depth=None, max_features='auto', max_leaf_nodes=None,
                    max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1,
                    min_samples_split=2, min_weight_fraction_leaf=0.0,
                    n_estimators=100, n_jobs=-1, oob_score=False,
                    random_state=123, verbose=0, warm_start=False)
regressor.fit(X_train, y_train)

#model Evaluation