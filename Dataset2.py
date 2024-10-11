import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 
dataset2 = pd.read_csv("dataset2.csv")

#PC usage on weekends
One_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 1])
Two_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 2])
Three_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 3])
Four_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 4])
Five_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 5])
Six_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 6])
Seven_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 7])

#PC usage on weekdays
One_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 1])
Two_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 2])
Three_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 3])
Four_Hour_PC_Weekday= len(dataset2[dataset2['C_wk'] == 4])
Five_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 5])
Six_Hour_PC_Weekday= len(dataset2[dataset2['C_wk'] == 6])
Seven_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 7])

#Amount on PC usage weekend and weekdays (can't be bother to repeat storing int with .5)
print("PC usage on weekends",
      "\n1 Hour PC usage: " + str(One_Hour_PC_Weekend),
      "\n2 Hour PC usage: " + str(Two_Hour_PC_Weekend),
      "\n3 Hour PC usage: " + str(Three_Hour_PC_Weekend),
      "\n4 Hour PC usage: " + str(Four_Hour_PC_Weekend),
      "\n5 Hour PC usage: " + str(Five_Hour_PC_Weekend),
      "\n6 Hour PC usage: " + str(Six_Hour_PC_Weekend),
      "\n7 Hour PC usage: " + str(Seven_Hour_PC_Weekend))

print("PC usage on weekdays",
      "\n1 Hour PC usage: " + str(One_Hour_PC_Weekday),
      "\n2 Hour PC usage: " + str(Two_Hour_PC_Weekday),
      "\n3 Hour PC usage: " + str(Three_Hour_PC_Weekday),
      "\n4 Hour PC usage: " + str(Four_Hour_PC_Weekday),
      "\n5 Hour PC usage: " + str(Five_Hour_PC_Weekday),
      "\n6 Hour PC usage: " + str(Six_Hour_PC_Weekday),
      "\n7 Hour PC usage: " + str(Seven_Hour_PC_Weekday))

Total_PC_we = ( One_Hour_PC_Weekend +
                Two_Hour_PC_Weekend +
                Three_Hour_PC_Weekend + 
                Four_Hour_PC_Weekend + 
                Five_Hour_PC_Weekend + 
                Six_Hour_PC_Weekend + 
                Seven_Hour_PC_Weekend)

Total_PC_wk = ( One_Hour_PC_Weekday +
                Two_Hour_PC_Weekday +
                Three_Hour_PC_Weekday + 
                Four_Hour_PC_Weekday+ 
                Five_Hour_PC_Weekday + 
                Six_Hour_PC_Weekday + 
                Seven_Hour_PC_Weekday)

print (f"Total: ", Total_PC_we + Total_PC_wk)


