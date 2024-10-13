#one -sample-t-test

import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 

# read csv into a DataFrame
dataset2 = pd.read_csv("dataset2.csv")
dataset3 = pd.read_csv("dataset3.csv")

merged_data = dataset2.merge(dataset3, on='ID', how='outer')
completed_rows = merged_data.dropna()

# inspect DataFrame content
print("Content of DataFrame: ")
print(completed_rows.info())
print(completed_rows.head())
print("")

# get only values (exclude header)
sample1 = completed_rows[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].to_numpy()
print(sample1)
sample2 = completed_rows[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 
                    'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 
                    'Loved', 'Intthg', 'Cheer']].to_numpy()
print(sample2)

# compute mean and standard deviation of the sample
print("Computing the basic statistics ...")
sample1_flat = sample1.flatten()
x_bar = st.tmean(sample1_flat)
s = st.tstd(sample1_flat)
print("\t Sample mean: %.2f" % x_bar)
print("\t Sample std. dev.: %.2f" % s)

sample2_flat = sample2.flatten()
x_bar = st.tmean(sample2_flat)
s = st.tstd(sample2_flat)
print("\t Sample mean: %.2f" % x_bar)
print("\t Sample std. dev.: %.2f" % s)

# perform one-sample t-test for sample1
# null hypothesis: population mean = 50
# alternative hypothesis: population mean > 50 (in the function below, note the argument 'greater')
t_stats1, p_val1 = st.ttest_1samp(sample1_flat, 50, alternative='greater')
print("\n Computing t* for sample1 ...")
print("\t t-statistic (t*): %.2f" % t_stats1)

print("\n Computing p-value for sample1 ...")
print("\t p-value: %.4f" % p_val1)

print("\n Conclusion for sample1:")
if p_val1 < 0.05:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")
    
# perform one-sample t-test for sample2
# null hypothesis: population mean = 50
# alternative hypothesis: population mean > 50 (in the function below, note the argument 'greater')
t_stats2, p_val2 = st.ttest_1samp(sample2_flat, 50, alternative='greater')
print("\n Computing t* for sample2 ...")
print("\t t-statistic (t*): %.2f" % t_stats2)

print("\n Computing p-value for sample2 ...")
print("\t p-value: %.4f" % p_val2)

print("\n Conclusion for sample2:")
if p_val2 < 0.05:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")
    
# create histogram for sample1
plt.figure(figsize=(8, 6))
plt.hist(sample1_flat, bins=20, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Sample 1')
plt.show()

# create histogram for sample2
plt.figure(figsize=(8, 6))
plt.hist(sample2_flat, bins=20, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Sample 2')
plt.show()