import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
dataset3 = pd.read_csv("dataset3.csv")

#Mean
Optm_mean = dataset3['Optm'].mean()
Usef_mean = dataset3['Usef'].mean()
Relx_mean = dataset3['Relx'].mean()
Intp_mean = dataset3['Intp'].mean()
Engs_mean = dataset3['Engs'].mean()
Dealpr_mean = dataset3['Dealpr'].mean()
Thcklr_mean = dataset3['Thcklr'].mean()
Goodme_mean = dataset3['Goodme'].mean()
Clsep_mean = dataset3['Clsep'].mean()
Conf_mean = dataset3['Conf'].mean()
Mkmind_mean = dataset3['Mkmind'].mean()
Loved_mean = dataset3['Loved'].mean()
Intthg_mean = dataset3['Intthg'].mean()
Cheer_mean = dataset3['Cheer'].mean()
print(f"Optimist Mean", Optm_mean) 
print(f"Useful Mean", Usef_mean)
print(f"Relax Mean", Relx_mean)
print(f"Interested Other People Mean", Intp_mean)
print(f"Energy Mean", Engs_mean)
print(f"Dealing Problem Mean", Dealpr_mean)
print(f"Thinking Clearly Mean", Thcklr_mean)
print(f"Good Mean", Goodme_mean)
print(f"Close Mean", Clsep_mean)
print(f"Confident Mean", Conf_mean)
print(f"Mind About Things Mean", Mkmind_mean)
print(f"Loved Mean", Loved_mean)
print(f"Interested New Things Mean", Intthg_mean)
print(f"Cheerful Mean", Cheer_mean)

#Median
Optm_median = dataset3['Optm'].median()
Usef_median = dataset3['Usef'].median()
Relx_median = dataset3['Relx'].median()
Intp_median = dataset3['Intp'].median()
Engs_median = dataset3['Engs'].mean()
Dealpr_median = dataset3['Dealpr'].median()
Thcklr_median = dataset3['Thcklr'].median()
Goodme_median = dataset3['Goodme'].median()
Clsep_median = dataset3['Clsep'].median()
Conf_median = dataset3['Conf'].median()
Mkmind_median = dataset3['Mkmind'].median()
Loved_median = dataset3['Loved'].median()
Intthg_median = dataset3['Intthg'].median()
Cheer_median = dataset3['Cheer'].median()
print()

print(f"Optimist median", Optm_median) 
print(f"Useful median", Usef_mean)
print(f"Relax median", Relx_mean)
print(f"Interested Other People median", Intp_median)
print(f"Energy median", Engs_median)
print(f"Dealing Problem median", Dealpr_median)
print(f"Thinking Clearly median", Thcklr_median)
print(f"Good median", Goodme_median)
print(f"Close median", Clsep_median)
print(f"Confident median", Conf_median)
print(f"Mind About Things median", Mkmind_median)
print(f"Loved median", Loved_median)
print(f"Interested New Things median", Intthg_median)
print(f"Cheerful median", Cheer_median)

#Mode
Optm_mode = dataset3['Optm'].mode()
Usef_mode = dataset3['Usef'].mode()
Relx_mode = dataset3['Relx'].mode()
Intp_mode = dataset3['Intp'].mode()
Engs_mode = dataset3['Engs'].mode()
Dealpr_mode = dataset3['Dealpr'].mode()
Thcklr_mode = dataset3['Thcklr'].mode()
Goodme_mode = dataset3['Goodme'].mode()
Clsep_mode = dataset3['Clsep'].mode()
Conf_mode = dataset3['Conf'].mode()
Mkmind_mode = dataset3['Mkmind'].mode()
Loved_mode = dataset3['Loved'].mode()
Intthg_mode = dataset3['Intthg'].mode()
Cheer_mode = dataset3['Cheer'].mode()
print()

print(f"Optimist mode", Optm_mode) 
print(f"Useful mode", Usef_mode)
print(f"Relax mode", Relx_mode)
print(f"Interested Other People mode", Intp_mode)
print(f"Energy mode", Engs_mode)
print(f"Dealing Problem mode", Dealpr_mode)
print(f"Thinking Clearly mode", Thcklr_mode)
print(f"Good mode", Goodme_mode)
print(f"Close mode", Clsep_mode)
print(f"Confident mode", Conf_mode)
print(f"Mind About Things mode", Mkmind_mode)
print(f"Loved mode", Loved_mode)
print(f"Interested New Things mode", Intthg_mode)
print(f"Cheerful mode", Cheer_mode)
print()

#Linear Regression 'Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer'
x = dataset3[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']] 
y = dataset3[''] #remove one of variable above and place it on y 

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse}')

nrmse = rmse / (y.max() - y.min())
print(f'Normalized Root Mean Squared Error: {nrmse}')

