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
    
# It calculates the counts of each unique value in the specified column, 
# creates a bar graph and a pie chart using the counts, and displays the graphs side by side.
def analyze(dataset, column):
    data = dataset

    counts = data[column].value_counts().sort_index()
    labels = counts.index
    sizes = counts.values

    plt.figure(figsize=(12, 6))

    # Bar graph
    plt.subplot(1, 2, 1)
    bars = plt.bar(labels, sizes, color='skyblue')
    plt.xlabel('Scores')
    plt.ylabel('Count')
    plt.title(f"Bar Graph of {column}")
    plt.xticks(labels)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Pie chart
    plt.subplot(1, 2, 2)
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f'{pct:.1f}%\n({val})'
        return my_format
    
    plt.pie(sizes, labels=labels, autopct=autopct_format(sizes), startangle=140)
    plt.title(f"Pie Chart of {column}")

    plt.tight_layout()
    plt.show()

# Create bar graph and pie chart for dataset1
for column in dataset1.columns[1:]:
    analyze(dataset1, column)

# Create bar graph and pie chart for dataset2
for column in dataset2.columns[1:]:
    analyze(dataset2, column)

# Create bar graph and pie chart for dataset3
for column in dataset3.columns[1:]:
    analyze(dataset3, column)