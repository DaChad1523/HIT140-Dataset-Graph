#z-score for dataset2 and dataset3

import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 

# Load dataset2 and dataset3 into pandas dataframes
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Calculate statistics for dataset2
x_bar2 = dataset2[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean().mean()
s2 = dataset2[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].std().mean()
n2 = len(dataset2)
print("Dataset2 - Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar2, s2, n2))

z_score2 = st.norm.ppf(q = 0.975)
print("Dataset2 - Z-statistic: %.2f" % z_score2)

std_err2 = s2 / math.sqrt(n2)
print("Dataset2 - Standard error: %.2f" % std_err2)

mrg_err2 = z_score2 * std_err2
print("Dataset2 - Margin of error: %.2f" % mrg_err2)

ci_low2 = x_bar2 - mrg_err2
ci_upp2 = x_bar2 + mrg_err2
print("Dataset2 - Confidence Interval of the mean: %.2f to %.2f" % (ci_low2, ci_upp2))

# Calculate statistics for dataset3
x_bar3 = dataset3[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 
                    'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 
                    'Loved', 'Intthg', 'Cheer']].mean().mean()
s3 = dataset3[['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 
                    'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 
                    'Loved', 'Intthg', 'Cheer']].std().mean()
n3 = len(dataset3)
print("Dataset3 - Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar3, s3, n3))

z_score3 = st.norm.ppf(q = 0.975)
print("Dataset3 - Z-statistic: %.2f" % z_score3)

std_err3 = s3 / math.sqrt(n3)
print("Dataset3 - Standard error: %.2f" % std_err3)

mrg_err3 = z_score3 * std_err3
print("Dataset3 - Margin of error: %.2f" % mrg_err3)

ci_low3 = x_bar3 - mrg_err3
ci_upp3 = x_bar3 + mrg_err3
print("Dataset3 - Confidence Interval of the mean: %.2f to %.2f" % (ci_low3, ci_upp3))

# Create a bar plot with error bars
means = [x_bar2, x_bar3]
errors = [mrg_err2, mrg_err3]
labels = ['Dataset2', 'Dataset3']

fig, ax = plt.subplots()
ax.bar(labels, means, yerr=errors, capsize=10)
ax.set_ylabel('Mean')
ax.set_title('Confidence Intervals of the Means')
ax.yaxis.grid(True)

plt.tight_layout()
plt.show()
