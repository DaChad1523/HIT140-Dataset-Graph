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
dataset2 = pd.read_csv("dataset2.csv")

#PC usage on weekends
Zero_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 0])
Half_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 0.5])
One_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 1])
Two_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 2])
Three_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 3])
Four_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 4])
Five_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 5])
Six_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 6])
Seven_Hour_PC_Weekend = len(dataset2[dataset2['C_we'] == 7])


#PC usage on weekdays
Zero_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 0])
Half_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 0.5])
One_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 1])
Two_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 2])
Three_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 3])
Four_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 4])
Five_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 5])
Six_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 6])
Seven_Hour_PC_Weekday = len(dataset2[dataset2['C_wk'] == 7])

#Video Game usage on weekends
Zero_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 0])
Half_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 0.5])
One_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 1])
Two_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 2])
Three_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 3])
Four_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 4])
Five_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 5])
Six_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 6])
Seven_Hour_VG_Weekend = len(dataset2[dataset2['G_we'] == 7])

#Video Game usage on weekdays
Zero_Hour_VG_Weekday= len(dataset2[dataset2['G_wk'] == 0])
Half_Hour_VG_Weekday= len(dataset2[dataset2['G_wk'] == 0.5])
One_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 1])
Two_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 2])
Three_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 3])
Four_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 4])
Five_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 5])
Six_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 6])
Seven_Hour_VG_Weekday = len(dataset2[dataset2['G_wk'] == 7])

#Smartphone usage on weekends
Zero_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 0])
Half_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 0.5])
One_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 1])
Two_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 2])
Three_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 3])
Four_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 4])
Five_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 5])
Six_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 6])
Seven_Hour_SP_Weekend = len(dataset2[dataset2['S_we'] == 7])

#Smartphone usage on weekdays
Zero_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 0])
Half_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 0.5])
One_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 1])
Two_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 2])
Three_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 3])
Four_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 4])
Five_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 5])
Six_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 6])
Seven_Hour_SP_Weekday = len(dataset2[dataset2['G_wk'] == 7])

#TV usage on weekends
Zero_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 0])
Half_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 0.5])
One_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 1])
Two_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 2])
Three_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 3])
Four_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 4])
Five_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 5])
Six_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 6])
Seven_Hour_TV_Weekend = len(dataset2[dataset2['T_we'] == 7])

#TV usage on weekdays
Zero_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 0])
Half_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 0.5])
One_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 1])
Two_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 2])
Three_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 3])
Four_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 4])
Five_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 5])
Six_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 6])
Seven_Hour_TV_Weekday = len(dataset2[dataset2['T_wk'] == 7])

#PC usage:
print("PC usage on weekends",
      "\n No PC usage: " + str(Zero_Hour_PC_Weekend),
      "\n1 Less then an hour PC usage: " + str(Half_Hour_PC_Weekend),
      "\n1 Hour PC usage: " + str(One_Hour_PC_Weekend),
      "\n2 Hour PC usage: " + str(Two_Hour_PC_Weekend),
      "\n3 Hour PC usage: " + str(Three_Hour_PC_Weekend),
      "\n4 Hour PC usage: " + str(Four_Hour_PC_Weekend),
      "\n5 Hour PC usage: " + str(Five_Hour_PC_Weekend),
      "\n6 Hour PC usage: " + str(Six_Hour_PC_Weekend),
      "\n7 Hour PC usage: " + str(Seven_Hour_PC_Weekend))
 

print("PC usage on weekdays",
      "\n No PC usage: " + str(Zero_Hour_PC_Weekday),
      "\n1 Less then an hour PC usage: " + str(Half_Hour_PC_Weekday),
      "\n1 Hour PC usage: " + str(One_Hour_PC_Weekday),
      "\n2 Hour PC usage: " + str(Two_Hour_PC_Weekday),
      "\n3 Hour PC usage: " + str(Three_Hour_PC_Weekday),
      "\n4 Hour PC usage: " + str(Four_Hour_PC_Weekday),
      "\n5 Hour PC usage: " + str(Five_Hour_PC_Weekday),
      "\n6 Hour PC usage: " + str(Six_Hour_PC_Weekday),
      "\n7 Hour PC usage: " + str(Seven_Hour_PC_Weekday))
print("")

#Video games usage:
print("Video game usage on weekends",
      "\n No VG usage: " + str(Zero_Hour_VG_Weekend),
      "\n1 Less then an hour VG usage: " + str(Half_Hour_VG_Weekend),
      "\n1 Hour VG usage: " + str(One_Hour_VG_Weekend),
      "\n2 Hour VG usage: " + str(Two_Hour_VG_Weekend),
      "\n3 Hour VG usage: " + str(Three_Hour_VG_Weekend),
      "\n4 Hour VG usage: " + str(Four_Hour_VG_Weekend),
      "\n5 Hour VG usage: " + str(Five_Hour_VG_Weekend),
      "\n6 Hour VG usage: " + str(Six_Hour_VG_Weekend),
      "\n7 Hour VG usage: " + str(Seven_Hour_VG_Weekend))

print("Video game usage on weekdays",
      "\n No VG usage: " + str(Zero_Hour_VG_Weekday),
      "\n1 Less then an hour VG usage: " + str(Half_Hour_VG_Weekday),
      "\n1 Hour VG usage: " + str(One_Hour_VG_Weekday),
      "\n2 Hour VG usage: " + str(Two_Hour_VG_Weekday),
      "\n3 Hour VG usage: " + str(Three_Hour_VG_Weekday),
      "\n4 Hour VG usage: " + str(Four_Hour_VG_Weekday),
      "\n5 Hour VG usage: " + str(Five_Hour_VG_Weekday),
      "\n6 Hour VG usage: " + str(Six_Hour_VG_Weekday),
      "\n7 Hour VG usage: " + str(Seven_Hour_VG_Weekday))
print("")

#Smart phone usage:
print("Smart phone usage on weekends",
      "\n No SP usage: " + str(Zero_Hour_SP_Weekend),
      "\n1 Less then an hour SP usage: " + str(Half_Hour_SP_Weekend),
      "\n1 Hour SP usage: " + str(One_Hour_SP_Weekend),
      "\n2 Hour SP usage: " + str(Two_Hour_SP_Weekend),
      "\n3 Hour SP usage: " + str(Three_Hour_SP_Weekend),
      "\n4 Hour SP usage: " + str(Four_Hour_SP_Weekend),
      "\n5 Hour SP usage: " + str(Five_Hour_SP_Weekend),
      "\n6 Hour SP usage: " + str(Six_Hour_SP_Weekend),
      "\n7 Hour SP usage: " + str(Seven_Hour_SP_Weekend))

print("Smart phone usage on weekdays",
      "\n No SP usage: " + str(Zero_Hour_SP_Weekday),
      "\n1 Less then an hour SP usage: " + str(Half_Hour_SP_Weekday),
      "\n1 Hour SP usage: " + str(One_Hour_SP_Weekday),
      "\n2 Hour SP usage: " + str(Two_Hour_SP_Weekday),
      "\n3 Hour SP usage: " + str(Three_Hour_SP_Weekday),
      "\n4 Hour SP usage: " + str(Four_Hour_SP_Weekday),
      "\n5 Hour SP usage: " + str(Five_Hour_SP_Weekday),
      "\n6 Hour SP usage: " + str(Six_Hour_SP_Weekday),
      "\n7 Hour SP usage: " + str(Seven_Hour_SP_Weekday))
print("")

#TV usage:
print("TV usage on weekends",
      "\n No TV usage: " + str(Zero_Hour_TV_Weekend),
      "\n1 Less then an hour TV usage: " + str(Half_Hour_TV_Weekend),
      "\n1 Hour TV usage: " + str(One_Hour_TV_Weekend),
      "\n2 Hour TV usage: " + str(Two_Hour_TV_Weekend),
      "\n3 Hour TV usage: " + str(Three_Hour_TV_Weekend),
      "\n4 Hour TV usage: " + str(Four_Hour_TV_Weekend),
      "\n5 Hour TV usage: " + str(Five_Hour_TV_Weekend),
      "\n6 Hour TV usage: " + str(Six_Hour_TV_Weekend),
      "\n7 Hour TV usage: " + str(Seven_Hour_TV_Weekend))

print("TV usage on weekdays",
      "\n No TV usage: " + str(Zero_Hour_TV_Weekday),
      "\n1 Less then an hour TV usage: " + str(Half_Hour_TV_Weekday),
      "\n1 Hour TV usage: " + str(One_Hour_TV_Weekday),
      "\n2 Hour TV usage: " + str(Two_Hour_TV_Weekday),
      "\n3 Hour TV usage: " + str(Three_Hour_TV_Weekday),
      "\n4 Hour TV usage: " + str(Four_Hour_TV_Weekday),
      "\n5 Hour TV usage: " + str(Five_Hour_TV_Weekday),
      "\n6 Hour TV usage: " + str(Six_Hour_TV_Weekday),
      "\n7 Hour TV usage: " + str(Seven_Hour_TV_Weekday))
print("")

#PC:
Total_PC_we = ( Zero_Hour_PC_Weekend +
                Half_Hour_PC_Weekend +        
                One_Hour_PC_Weekend +
                Two_Hour_PC_Weekend +
                Three_Hour_PC_Weekend + 
                Four_Hour_PC_Weekend + 
                Five_Hour_PC_Weekend + 
                Six_Hour_PC_Weekend + 
                Seven_Hour_PC_Weekend)

Total_PC_wk = ( Zero_Hour_PC_Weekday +
                Half_Hour_PC_Weekday +
                One_Hour_PC_Weekday +
                Two_Hour_PC_Weekday +
                Three_Hour_PC_Weekday + 
                Four_Hour_PC_Weekday + 
                Five_Hour_PC_Weekday + 
                Six_Hour_PC_Weekday + 
                Seven_Hour_PC_Weekday)
#Video Games:
Total_VG_we = ( Zero_Hour_VG_Weekend +
                Half_Hour_VG_Weekend +
                One_Hour_VG_Weekend +
                Two_Hour_VG_Weekend +
                Three_Hour_VG_Weekend + 
                Four_Hour_VG_Weekend + 
                Five_Hour_VG_Weekend + 
                Six_Hour_VG_Weekend + 
                Seven_Hour_VG_Weekend)

Total_VG_wk = ( Zero_Hour_VG_Weekday +
                Half_Hour_VG_Weekday +
                One_Hour_VG_Weekday +
                Two_Hour_VG_Weekday +
                Three_Hour_VG_Weekday + 
                Four_Hour_VG_Weekday + 
                Five_Hour_VG_Weekday + 
                Six_Hour_VG_Weekday + 
                Seven_Hour_VG_Weekday)
#Smartphone:
Total_SP_we = ( Zero_Hour_SP_Weekend +
                Half_Hour_SP_Weekend +
                One_Hour_SP_Weekend +
                Two_Hour_SP_Weekend +
                Three_Hour_SP_Weekend + 
                Four_Hour_SP_Weekend + 
                Five_Hour_SP_Weekend + 
                Six_Hour_SP_Weekend + 
                Seven_Hour_SP_Weekend)

Total_SP_wk = ( Zero_Hour_SP_Weekday +
                Half_Hour_SP_Weekday +
                One_Hour_SP_Weekday +
                Two_Hour_SP_Weekday +
                Three_Hour_SP_Weekday + 
                Four_Hour_SP_Weekday + 
                Five_Hour_SP_Weekday + 
                Six_Hour_SP_Weekday + 
                Seven_Hour_SP_Weekday)
#TV:
Total_TV_we = ( Zero_Hour_TV_Weekend +
                Half_Hour_TV_Weekend +
                One_Hour_TV_Weekend +
                Two_Hour_TV_Weekend +
                Three_Hour_TV_Weekend + 
                Four_Hour_TV_Weekend + 
                Five_Hour_TV_Weekend + 
                Six_Hour_TV_Weekend + 
                Seven_Hour_TV_Weekend)

Total_TV_wk = ( Zero_Hour_TV_Weekday +
                Half_Hour_TV_Weekday +
                One_Hour_TV_Weekday +
                Two_Hour_TV_Weekday +
                Three_Hour_TV_Weekday + 
                Four_Hour_TV_Weekday + 
                Five_Hour_TV_Weekday + 
                Six_Hour_TV_Weekday + 
                Seven_Hour_TV_Weekday)
print("")
print(f"PC weekend: ", Total_PC_we)
print(f"PC weekday: ", Total_PC_wk)

print(f"Video game weekend: ", Total_VG_we)
print(f"Video game weekday: ", Total_VG_wk)

print(f"Smartphone weekend: ", Total_SP_we)
print(f"Smartphone weekday: ", Total_SP_wk)

print(f"TSmartphone weekend: ", Total_TV_we)
print(f"Smartphone weekday: ", Total_TV_wk)
print("")
print (f"Total: ", Total_PC_we + Total_PC_wk + Total_VG_we + Total_VG_wk + Total_SP_we + Total_SP_wk + Total_TV_we + Total_TV_wk)

print()
#Finding the Mean
PC_Mean_We = dataset2['C_we'].mean()
PC_Mean_Wk = dataset2['C_wk'].mean()

VG_Mean_We = dataset2['G_we'].mean()
VG_Mean_Wk = dataset2['G_wk'].mean()

SP_Mean_We = dataset2['S_we'].mean()
SP_Mean_Wk = dataset2['S_wk'].mean()

TV_Mean_We = dataset2['T_we'].mean()
TV_Mean_Wk = dataset2['T_wk'].mean()

print(f"Average PC weekend usage: ", PC_Mean_We)
print(f"Average PC weekday usage: ", PC_Mean_Wk)
print(f"Average VG weekend usage: ", VG_Mean_We)
print(f"Average VG weekday usage: ", VG_Mean_Wk)
print(f"Average SP weekend usage: ", SP_Mean_We)
print(f"Average SP weekday usage: ", SP_Mean_Wk)
print(f"Average TV weekend usage: ", TV_Mean_We)
print(f"Average TV weekday usage: ", TV_Mean_Wk)
print()
#Linear Regression model
x = dataset2[['C_we','C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']] #'C_we','C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk'
y = dataset2[''] #input ur variable but you have to get rid of the variable above it ^
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

"""
plt.scatter(y_test, y_pred, color='blue', label='Actual vs Predicted')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.show()
"""