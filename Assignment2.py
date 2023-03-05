import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
sales_df = pd.read_csv('sales_data_na.csv')

# check the size of the dataset
print("Number of rows:", sales_df.shape[0])
print("Number of columns:", sales_df.shape[1])

# check for missing data
print(sales_df.isnull().sum())

# check for duplicates
print("Number of duplicate rows:", sales_df.duplicated().sum())

# check for outliers
sns.boxplot(x=sales_df['Profit'])

# drop duplicate rows
sales_df.drop_duplicates(inplace=True)

# rename columns to make them consistent
sales_df.rename(columns={'Product_Category': 'Category', 'Sub_Category': 'Subcategory', 'Unit_Cost': 'Cost', 'Unit_Price': 'Price'}, inplace=True)

# Replace 'Aogust' with 'August'
sales_df['Month'] = sales_df['Month'].str.replace('Aogust', 'August')

# Replace 'Marsh' with 'March'
sales_df['Month'] = sales_df['Month'].str.replace('Marsh', 'March')

# Replace 'Jone' with 'June'
sales_df['Month'] = sales_df['Month'].str.replace('Jone', 'June')

# Replace 'Joly' with 'July'
sales_df['Month'] = sales_df['Month'].str.replace('Joly', 'July')

# tidy the dataset by converting month names to numbers
sales_df['Month'] = pd.to_datetime(sales_df['Month'], format='%B').dt.month

# convert data types to correct format
sales_df['Order_Quantity'] = sales_df['Order_Quantity'].astype('int64')
sales_df['Cost'] = sales_df['Cost'].astype('float64')
sales_df['Price'] = sales_df['Price'].astype('float64')
sales_df['Profit'] = sales_df['Profit'].astype('float64')
sales_df['Revenue'] = sales_df['Revenue'].astype('float64')

# plot the relationship between profit and revenue
sns.scatterplot(x=sales_df['Profit'], y=sales_df['Revenue'])

# plot the distribution of ages
sns.histplot(data=sales_df, x='Customer_Age', bins=10)

# plot the number of sales per category
sns.countplot(data=sales_df, x='Category')
