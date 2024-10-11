import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 
dataset1 = pd.read_csv("dataset1.csv")

#Amount
Male = dataset1[dataset1['gender'] == 1]
Gender_Other = dataset1[dataset1['gender'] == 0]

#Mean
Mean_Male = Male['gender'].mean()
Mean_Male_Other = Gender_Other['gender'].mean()

Minority = dataset1[dataset1['minority'] == 1]
Minority_Other = dataset1[dataset1['minority'] == 0]

Deprived = dataset1[dataset1['deprived'] == 1]
Deprived_Other = dataset1[dataset1['deprived'] == 0]

#Gender
print("Currently Male Quantity: " + str(len(Male)),  "\nOther Quantity: " + str(len(Gender_Other)))

#Minortiy
print("Currently Minortiy Quantity: " + str(len(Minority)),  "\nOther Quantity: " + str(len(Minority_Other)))

#Deprived
print("Currently Deprived Quantity: " + str(len(Deprived)),  "\nOther Quantity: " + str(len(Deprived_Other)))