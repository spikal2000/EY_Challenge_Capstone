# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:30:57 2023

@author: spika
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor


data = pd.read_csv("newshit.csv")
#replace District
data['District'].unique()
district_mapping = {'Chau_Phu': 0, 'Chau_Thanh': 1, 'Thoai_Son': 2}
data['District'] = data['District'].replace(district_mapping)
#Replace Rice Crop Intensity(D=Double, T=Triple)
data['Rice Crop Intensity(D=Double, T=Triple)'].unique()
intensity_mapping = {'T':0, 'D':1}
data['Rice Crop Intensity(D=Double, T=Triple)'] = data['Rice Crop Intensity(D=Double, T=Triple)'].replace(intensity_mapping)
#Replace Rice Crop Intensity(D=Double, T=Triple)
data['Season(SA = Summer Autumn, WS = Winter Spring)'].unique()
seasson_mapping = {'SA':0, 'WS':1}
data['Season(SA = Summer Autumn, WS = Winter Spring)'] = data['Season(SA = Summer Autumn, WS = Winter Spring)'].replace(seasson_mapping)

crop_data = pd.read_csv("Crop_Yield_Data_challenge_2.csv")


X = data
y = crop_data['Rice Yield (kg/ha)']

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=21)

"""
ExtraTreesRegressor
"""

def ExtraTreesR(X_train, y_train, n_estimators=100, max_depth=None, min_samples_split=2,max_features='auto',
                min_samples_leaf=2, bootstrap=False, warm_start=False):
# def ExtraTreesR(X_train, y_train):
    
    regressor = ExtraTreesRegressor(n_estimators=n_estimators, 
                                    max_depth=max_depth,
                                    min_samples_split=min_samples_split,
                                    max_features=max_features,
                                    min_samples_leaf = min_samples_leaf,
                                    bootstrap=bootstrap,
                                    warm_start=warm_start
                                    )
    {'friedman_mse', 'absolute_error', 'squared_error', 'poisson'}
   
    # regressor = ExtraTreesRegressor(bootstrap=True, ccp_alpha=0.0, criterion='absolute_error',
    #                 max_depth=15, max_features='auto', max_leaf_nodes=None,
    #                 max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1,
    #                 min_samples_split=2, min_weight_fraction_leaf=0.0,
    #                 n_estimators=500, n_jobs=-1, oob_score=False,
    #                 random_state=123, verbose=0, warm_start=False)
    regressor.fit(X_train, y_train)
    #model Evaluation
    print("============ExtraTreesRegressor============")
    #In sample evaluation
    insample_predictions = regressor.predict(X_train)
    insample_r2 = r2_score(y_train,insample_predictions)
    insample_mae = mean_absolute_error(y_train, insample_predictions)
    insample_mse = mean_squared_error(y_train, insample_predictions)
    insample_rmse = np.sqrt(insample_mse)
    print("Insample R2 Score: {0:.2f}".format(insample_r2))
    print("Insample MAE: {0:.2f}".format(insample_mae))
    print("Insample MSE: {0:.2f}".format(insample_mse))
    print("Insample RMSE: {0:.2f}".format(insample_rmse))
    
    print("___________________________________________________")
    #Out-sample evaluation
    outsample_predictions = regressor.predict(X_test)
    outsample_r2 = r2_score(y_test, outsample_predictions)
    outsample_mae = mean_absolute_error(y_test, outsample_predictions)
    outsample_mse = mean_squared_error(y_test, outsample_predictions)
    outsample_rmse = np.sqrt(outsample_mse)
    
    print("Outsample R2 Score: {0:.2f}".format(outsample_r2))
    print("Outsample MAE: {0:.2f}".format(outsample_mae))
    print("Outsample MSE: {0:.2f}".format(outsample_mse))
    print("Outsample RMSE: {0:.2f}".format(outsample_rmse))
   
    
    return regressor

def ExtraTreesR_feature_selection(X_train, y_train):
    regressor = ExtraTreesRegressor(n_estimators=100, max_depth=None, min_samples_split=2, max_features='auto', min_samples_leaf=2, bootstrap=False, warm_start=False)
    regressor.fit(X_train, y_train)

    feature_importances = regressor.feature_importances_
    feature_importance_dict = dict(zip(X_train.columns, feature_importances))
    feature_importance_dict_sorted = sorted(feature_importance_dict.items(), key=lambda item: item[1], reverse=True)

    return feature_importance_dict_sorted


"""
Random Forest
"""
def RandomForestR(X_train, y_train, X_test, y_test):
    rfr = RandomForestRegressor()
    
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 15, 20],
        'min_samples_split': [2, 5, 10],
        'max_features': ['auto', 'sqrt'],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    }
    
    grid_search = GridSearchCV(estimator=rfr, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)
    # rfr = RandomForestRegressor(n_estimators=300,
    #                           max_depth=15,
    #                           min_samples_split=5,
    #                           max_features='auto',
    #                           min_samples_leaf=2,
    #                           bootstrap=True)

    # rfr.fit(X_train, y_train)
    print("Best parameters found: ", grid_search.best_params_)

    best_rfr = grid_search.best_estimator_
    # In-sample evaluation
    insample_predictions = best_rfr.predict(X_train)
    insample_r2 = r2_score(y_train, insample_predictions)
    insample_mae = mean_absolute_error(y_train, insample_predictions)
    insample_mse = mean_squared_error(y_train, insample_predictions)
    insample_rmse = np.sqrt(insample_mse)
    print("Insample R2 Score: {0:.2f}".format(insample_r2))
    print("Insample MAE: {0:.2f}".format(insample_mae))
    print("Insample MSE: {0:.2f}".format(insample_mse))
    print("Insample RMSE: {0:.2f}".format(insample_rmse))
    
    print("___________________________________________________")
    # Out-sample evaluation
    outsample_predictions = best_rfr.predict(X_test)
    outsample_r2 = r2_score(y_test, outsample_predictions)
    outsample_mae = mean_absolute_error(y_test, outsample_predictions)
    outsample_mse = mean_squared_error(y_test, outsample_predictions)
    outsample_rmse = np.sqrt(outsample_mse)
    
    print("Outsample R2 Score: {0:.2f}".format(outsample_r2))
    print("Outsample MAE: {0:.2f}".format(outsample_mae))
    print("Outsample MSE: {0:.2f}".format(outsample_mse))
    print("Outsample RMSE: {0:.2f}".format(outsample_rmse))
   
    return best_rfr, insample_r2, outsample_r2


#model_rf, ir2, or2 = RandomForestR(X_train, y_train, X_test, y_test)




# model = ExtraTreesR(X_train, y_train)

"""
# Use the ExtraTreesRegressor
model = ExtraTreesR(X_train, y_train, 
                    n_estimators=110, 
                    max_depth=5, 
                    min_samples_split=10,max_features='auto',
               bootstrap=True)

model = ExtraTreesR(X_train, y_train, 
                    n_estimators=300, 
                    max_depth=8, 
                    min_samples_split=6,
                    max_features='auto',
                    min_samples_leaf=10,
                bootstrap=True,
                warm_start=True)

new_data = X_test[:4]
y_new = y_test[:4]
predctions = model.predict(new_data)

print("Actual:", y_new, "Predicted:", predctions)
"""
feature_importances = ExtraTreesR_feature_selection(X_train, y_train)
for feature, importance in feature_importances:
    print(f"Feature: {feature}, Importance: {importance}")

