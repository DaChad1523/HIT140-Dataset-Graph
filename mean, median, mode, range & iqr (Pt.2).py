#mean, median, mode, range & iqr for dataset1, dataset2, & dataset3

import pandas as pd
import statistics as stat
import numpy as np
import math
import scipy.stats as st
import statsmodels
import matplotlib.pyplot as plt 

# Load the datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Calculates statistics for dataset1
print("Dataset 1:")
for column in dataset1.columns[1:]:
    data = dataset1[column].tolist()
    mean = np.mean(data)
    median = np.median(data)
    mode = st.mode(data)
    the_range = np.max(data) - np.min(data)
    pct25 = np.percentile(data, 25)
    pct75 = np.percentile(data, 75)
    iqr = pct75 - pct25
    print(f"Column: {column}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Range: {the_range}")
    print(f"IQR: {iqr:.2f}")
    print()

# Calculates statistics for dataset2
print("Dataset 2:")
for column in dataset2.columns[1:]:
    data = dataset2[column].tolist()
    mean = np.mean(data)
    median = np.median(data)
    mode = st.mode(data)
    the_range = np.max(data) - np.min(data)
    pct25 = np.percentile(data, 25)
    pct75 = np.percentile(data, 75)
    iqr = pct75 - pct25
    print(f"Column: {column}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Range: {the_range}")
    print(f"IQR: {iqr:.2f}")
    print()

# Calculates statistics for dataset3
print("Dataset 3:")
for column in dataset3.columns[1:]:
    data = dataset3[column].tolist()
    mean = np.mean(data)
    median = np.median(data)
    mode = st.mode(data)
    the_range = np.max(data) - np.min(data)
    pct25 = np.percentile(data, 25)
    pct75 = np.percentile(data, 75)
    iqr = pct75 - pct25
    print(f"Column: {column}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Range: {the_range}")
    print(f"IQR: {iqr:.2f}")
    print()
    
# Create bar plots for dataset1
plt.figure(figsize=(10, 6))
dataset1.iloc[:, 1:].mean().plot(kind='bar')
plt.xlabel('Columns')
plt.ylabel('Mean')
plt.title('Bar Plot - Dataset 1')
plt.tight_layout()
plt.show()

# Create pie chart for dataset1
plt.figure(figsize=(8, 8))
plt.pie(dataset1.iloc[:, 1:].mean(), labels=dataset1.columns[1:], autopct='%1.1f%%')
plt.title('Pie Chart - Dataset 1')
plt.tight_layout()
plt.show()

# Create bar plots for dataset2
plt.figure(figsize=(10, 6))
dataset2.iloc[:, 1:].mean().plot(kind='bar')
plt.xlabel('Columns')
plt.ylabel('Mean')
plt.title('Bar Plot - Dataset 2')
plt.tight_layout()
plt.show()

# Create pie chart for dataset2
plt.figure(figsize=(8, 8))
plt.pie(dataset2.iloc[:, 1:].mean(), labels=dataset2.columns[1:], autopct='%1.1f%%')
plt.title('Pie Chart - Dataset 2')
plt.tight_layout()
plt.show()

# Create bar plots for dataset3
plt.figure(figsize=(10, 6))
dataset3.iloc[:, 1:].mean().plot(kind='bar')
plt.xlabel('Columns')
plt.ylabel('Mean')
plt.title('Bar Plot - Dataset 3')
plt.tight_layout()
plt.show()

# Create pie chart for dataset3
plt.figure(figsize=(8, 8))
plt.pie(dataset3.iloc[:, 1:].mean(), labels=dataset3.columns[1:], autopct='%1.1f%%')
plt.title('Pie Chart - Dataset 3')
plt.tight_layout()
plt.show()

# Calculate means for each column in the datasets
means1 = [np.mean(dataset1[column].tolist()) for column in dataset1.columns[1:]]
means2 = [np.mean(dataset2[column].tolist()) for column in dataset2.columns[1:]]
means3 = [np.mean(dataset3[column].tolist()) for column in dataset3.columns[1:]]

# Find the maximum number of columns among the datasets
max_columns = max(len(means1), len(means2), len(means3))

# Create a bar chart comparing the means
x = np.arange(max_columns)
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, means1 + [0] * (max_columns - len(means1)), width, label='Dataset 1')
rects2 = ax.bar(x, means2 + [0] * (max_columns - len(means2)), width, label='Dataset 2')
rects3 = ax.bar(x + width, means3 + [0] * (max_columns - len(means3)), width, label='Dataset 3')

ax.set_ylabel('Mean')
ax.set_title('Comparison of Means Across Datasets')
ax.set_xticks(x)
ax.set_xticklabels([f'Column {i+1}' for i in range(max_columns)])
ax.legend()

plt.tight_layout()
plt.show()