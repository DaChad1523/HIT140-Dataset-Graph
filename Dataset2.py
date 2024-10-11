import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 
dataset2 = pd.read_csv("dataset2.csv")

#PC usage on weekends
One_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 1]
Two_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 2]
Three_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 3]
Four_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 4]
Five_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 5]
Six_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 6]
Seven_Hour_PC_Weekend = dataset2[dataset2['C_we'] == 7]

#PC usage on weekdays
One_Hour_PC_Weekday = dataset2[dataset2['C_we'] == 1]
Two_Hour_PC_Weekday = dataset2[dataset2['C_we'] == 2]
Three_Hour_PC_Weekday = dataset2[dataset2['C_we'] == 3]
Four_Hour_PC_Weekday= dataset2[dataset2['C_we'] == 4]
Five_Hour_PC_Weekday = dataset2[dataset2['C_we'] == 5]
Six_Hour_PC_Weekday= dataset2[dataset2['C_we'] == 6]
Seven_Hour_PC_Weekday = dataset2[dataset2['C_we'] == 7]

len(print(One_Hour_PC_Weekend))