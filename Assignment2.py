import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
sales_data_url = "https://raw.githubusercontent.com/mc220517312/Assignment-2/main/sales_data_na.csv"
sales_data_before_cleaning = pd.read_csv(sales_data_url, sep=',')

# Box plot of revenue before cleaning
plt.boxplot(sales_data_before_cleaning['Revenue'])
plt.title('Box plot of revenue before cleaning')
plt.show()

# Clean the data
sales_data = sales_data_before_cleaning.copy()
sales_data.columns = sales_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
sales_data = sales_data.drop_duplicates()
sales_data = sales_data.dropna()

# Box plot of revenue after cleaning
plt.boxplot(sales_data['revenue'])
plt.title('Box plot of revenue after cleaning')
plt.show()

# Most Profitable Year
profit_by_year = sales_data.groupby('year')['profit'].sum()
profit_by_year.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.title('Profit by Year')
plt.show()

# Most Profitable Month
profit_by_month = sales_data.groupby('month')['profit'].sum()
profit_by_month.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Profit by Month')
plt.show()

# Gender Having Most Order
order_by_gender = sales_data.groupby('customer_gender')['order_quantity'].sum()
order_by_gender.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Order Quantity')
plt.title('Order Quantity by Gender')
plt.show()

# Correlation between Annual Sales
annual_sales = sales_data.groupby('year')['revenue'].sum()
annual_sales.plot(kind='line', marker='o')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Annual Sales')
plt.show()

# Category Generates Most Profit
profit_by_category = sales_data.groupby('product_category')['profit'].sum()
profit_by_category.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Profit by Category')
plt.show()

# Sub-Category Generates Most Profit
profit_by_subcategory = sales_data.groupby('sub_category')['profit'].sum()
profit_by_subcategory.plot(kind='bar')
plt.xlabel('Sub-Category')
plt.ylabel('Profit')
plt.title('Profit by Sub-Category')
plt.show()

# Sales per Country
sales_by_country = sales_data.groupby('country')['revenue'].sum()
sales_by_country.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Country')
plt.show()
