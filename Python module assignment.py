#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


# Load the dataset
df = pd.read_csv("myexcel.csv")  # Ensure the file name matches

# Correct the "height" column by replacing values with random numbers between 150 and 180
np.random.seed(42)  # Ensures reproducibility
df["height"] = np.random.randint(150, 181, size=len(df))

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values (if required)
df.fillna(method="ffill", inplace=True)  # Forward fill as an example


# In[7]:


team_counts = df["Team"].value_counts()
team_percentage = (team_counts / len(df)) * 100

# Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=team_counts.index, y=team_counts.values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Teams")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employees Across Teams")
plt.show()

print("Percentage of employees per team:\n", team_percentage)


# In[8]:


position_counts = df["Position"].value_counts()

# Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=position_counts.index, y=position_counts.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel("Positions")
plt.ylabel("Number of Employees")
plt.title("Employee Count by Position")
plt.show()


# In[9]:


age_bins = [20, 30, 40, 50, 60]  # Define age groups
df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=["20-30", "30-40", "40-50", "50-60"])
age_group_counts = df["Age Group"].value_counts()

# Visualization
plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette="Blues_r")
plt.xlabel("Age Groups")
plt.ylabel("Number of Employees")
plt.title("Predominant Age Group of Employees")
plt.show()

print("Most common age group:", age_group_counts.idxmax())


# In[10]:


team_salary = df.groupby("Team")["Salary"].sum().sort_values(ascending=False)
position_salary = df.groupby("Position")["Salary"].sum().sort_values(ascending=False)

# Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=team_salary.index, y=team_salary.values, palette="magma")
plt.xticks(rotation=45)
plt.xlabel("Teams")
plt.ylabel("Total Salary Expense")
plt.title("Total Salary Expenditure by Team")
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=position_salary.index, y=position_salary.values, palette="rocket")
plt.xticks(rotation=45)
plt.xlabel("Positions")
plt.ylabel("Total Salary Expense")
plt.title("Total Salary Expenditure by Position")
plt.show()

print("Highest salary expenditure - Team:", team_salary.idxmax())
print("Highest salary expenditure - Position:", position_salary.idxmax())


# In[11]:


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Age"], y=df["Salary"], alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Correlation Between Age and Salary")
plt.show()

# Calculate correlation
correlation = df["Age"].corr(df["Salary"])
print(f"Correlation between Age and Salary: {correlation:.2f}")


# In[ ]:




