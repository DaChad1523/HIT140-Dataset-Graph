import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 
dataset3 = pd.read_csv("dataset3.csv")
dataset2 = pd.read_csv("dataset2.csv")

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