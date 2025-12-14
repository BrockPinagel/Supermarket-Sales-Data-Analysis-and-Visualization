"""
Brock Pinagel
Dr. Yash Patel
INT6103: Python for Data Analysis and Visualization
18 December 2025
Final Project - Supermarket Sales Data Analysis and Visualization
"""
import numpy as np # Numerical computing
import matplotlib.pyplot as plt # Data visualization
import pandas as pd # Data manipulation
import seaborn as sns # Advanced data visualization
import statsmodels.api as sm # Statistical modeling
from scipy.stats import pearsonr # Statistical tests
from sklearn.linear_model import LinearRegression # Regression analysis

# Load dataset
df = pd.read_csv('Supermarket Sales 2.csv')
# print(df.head())
# print(df.columns)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")                 

# Calculate Total
df['Total'] = df['Unit price'] * df['Quantity']

# Descriptive Statistics
print("------------------Descriptive Statistics-------------------")
print(df[['Unit price', 'Quantity', 'Total', 'Rating']].describe())

# Frequency counts
print("------------------Frequency Counts-------------------")
print(df['Gender'].value_counts())
print(df['Product line'].value_counts())

# Grouped statistics
print("------------------Grouped Statistics-------------------")   
print("------------------Total Sales by Product Line-------------------")   
print(df.groupby('Product line')['Total'].sum())
print("------------------Quantity Sold by Product Line-------------------") 
print(df.groupby('Product line')['Quantity'].sum())

# Correlation matrix
df.corr(numeric_only=True)

# Significance testing
corr, p = pearsonr(df['Unit price'], df['Total'])
print("------------------Pearson Correlation-------------------")
print("Pearson correlation coefficient:", corr)
print(f"P-value: {p:.5f}")

# linear regression
x = df[['Unit price']]
y = df['Total']

model = LinearRegression().fit(x, y)

print("-----------------------LR-----------------------------")
print("Coefficient:", model.coef_[0])
print('Intercept:', model.intercept_)
print('R^2:', model.score(x, y))

# Multiple Regression
numeric_df = df.select_dtypes(include='number').drop(columns=['Total'])
x = numeric_df
y = df['Total']

model = LinearRegression().fit(x,y)

print("-----------------------MR-----------------------------")
print("Coefficients:", model.coef_)
print('R^2:', model.score(x, y))

# Data visualization Dashboard
plt.figure(figsize=(18, 20))

# Monthly total sales format conversion
df['Month'] = df['Date'].dt.strftime('%b')  
monthly_sales = df.groupby('Month')['Total'].sum().reindex([
    'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
], fill_value=0)

# Average order value by customer type
aov = df.groupby('Customer type')['Total'].mean().reset_index()

# Total sales per branch
branch_sales = df.groupby('Branch')['Total'].sum()

# Histogram
plt.subplot(3, 2, 1)
# plt.figure(figsize=(12, 8))
sns.histplot(df['Total'], kde=True)
plt.title('Distribution of Transaction Values')
# plt.show()

# Box plot
plt.subplot(3, 2, 2)
# plt.figure(figsize=(12, 8))
sns.boxplot(x='Branch', y='Rating', data=df)
plt.title('Average Rating by Branch')
# plt.show()

# Line plot
plt.subplot(3, 2, 3)
# plt.figure(figsize=(12, 8))
plt.plot(monthly_sales.index, monthly_sales.values, color='darkblue')
plt.title("Monthly Total Sales", pad=20)
plt.xlabel("Month")
plt.ylabel("Total Sales")
# plt.show()

# Correlation heatmap 
plt.subplot(3, 2, 4) 
# plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm') 
plt.title('Correlation Matrix') 
plt.yticks(rotation=0) 
plt.xticks(rotation=45)
# plt.show()

# Bar Chart
plt.subplot(3, 2, 5)
# plt.figure(figsize=(12, 8))
sns.barplot(data=aov, x='Customer type', y='Total')
plt.title("Average Order Value by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Average Order Value")
# plt.show()

# Pie Chart
plt.subplot(3, 2, 6)
# plt.figure(figsize=(12, 8))
plt.pie(branch_sales, labels=branch_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Percentage of Total Sales by Branch")
plt.axis('equal')
# plt.show()

# Show dashboard
plt.tight_layout()
plt.subplots_adjust(top=0.97, hspace=0.45, bottom=0.05, wspace=0.18)
plt.show()

# Statsmodels OLS Regression
X = df[['Unit price']]
X = sm.add_constant(X)
y = df['Total']

model = sm.OLS(y, X).fit()
print(model.summary())