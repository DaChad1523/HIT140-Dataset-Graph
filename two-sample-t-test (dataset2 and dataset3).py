#two-sample-t-test

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

# split DataFrame into two subsets: 
# Id1: 1000002, 1000003, 1000004... and so on
# Id2: 1087360, 1094049, 1094067... and so on
Id1 = completed_rows[completed_rows["ID"] < 1120115]
Id2 = completed_rows[completed_rows["ID"] >= 1091115]


# select relevant column from each DataFrame
sample1 = Id1[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].to_numpy()
sample2 = Id2[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 
                    'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 
                    'Loved', 'Intthg', 'Cheer']].to_numpy()


# print values in samples
print("Sample 1: ", sample1)
print("Sample 2: ", sample2)


# compute basic statistics for two samples
print("\n Computing basic statistics of samples ...")

# the basic statistics of sample 1:
x_bar1 = np.mean(sample1, axis=0)
s1 = np.std(sample1, axis=0)
n1 = len(sample1)
print("\t Statistics of sample 1:")
for i in range(len(x_bar1)):
    print(f"\t\t Column {i+1}: {x_bar1[i]:.3f} (mean), {s1[i]:.3f} (std. dev.)")
print(f"\t\t Sample size: {n1}")

# the basic statistics of sample 2:
x_bar2 = np.mean(sample2, axis=0)
s2 = np.std(sample2, axis=0)
n2 = len(sample2)
print("\t Statistics of sample 2:")
for i in range(len(x_bar2)):
    print(f"\t\t Column {i+1}: {x_bar2[i]:.3f} (mean), {s2[i]:.3f} (std. dev.)")
print(f"\t\t Sample size: {n2}")


# perform two-sample t-test
# null hypothesis: mean of sample 1 = mean of sample 2
# alternative hypothesis: mean of sample 1 is greater than mean of sample 2 (one-sided test)
# note the argument equal_var=False, which assumes that two populations do not have equal variance
# perform two-sample t-test for each pair of corresponding columns
print("\n Performing two-sample t-test for each pair of corresponding columns...")
for i in range(min(len(x_bar1), len(x_bar2))):
    t_stat, p_val = st.ttest_ind_from_stats(x_bar1[i], s1[i], n1, x_bar2[i], s2[i], n2, equal_var=False, alternative='greater')
    print(f"\n Column pair {i+1}:")
    print(f"\t t-statistic (t*): {t_stat:.2f}")
    print(f"\t p-value: {p_val:.4f}")

print("\n Conclusion:")
if p_val < 0.05:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")
    
# create a bar plot to visualize the mean values of each column pair
column_pairs = [f"Pair {i+1}" for i in range(min(len(x_bar1), len(x_bar2)))]
x = np.arange(len(column_pairs))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, x_bar1[:len(column_pairs)], width, label='Sample 1')
rects2 = ax.bar(x + width/2, x_bar2[:len(column_pairs)], width, label='Sample 2')

ax.set_ylabel('Mean Value')
ax.set_title('Comparison of Mean Values between Sample 1 and Sample 2 in Column Pairs')
ax.set_xticks(x)
ax.set_xticklabels(column_pairs)
ax.legend()

fig.tight_layout()
plt.show()