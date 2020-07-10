# Import necessary libraries

import pandas as pd
import matlotlib.pyplot as plt

# Import the dataset from assigned path

path = 'C://Users/mca/Desktop/New folder/Online_Retail.csv'

# Read the data set ( for std encoding we use latin1 )

online_retail = pd.read_csv(path, encoding = 'latin1')

# Display the dataset columns

#print(online_retail.columns)

# Display total rows and columns

#print(online_retail.shape)

# Display the dataset first five rows

#print(online_retail.head())

# Display the whole dataset records

#print(online_retail)

# Display the dataset information

#print(online_retail.info())

# Display the dataset single column value

#print(online_retail.Country)

# Display the dataset mean, medium and other values

#print(online_retail.describe())

#for finding missing data

#print(online_retail['Country'].isnull()

#print(online_retail.isnull())

#Make a list of missing value pattern
# Replace missing values with a number
#online_retail['Country'].fillna('india', inplace=True)
#print(online_retail)

#fill data using median

# Replace using median

#print(online_retail['CustomerID'].isnull())

#median = online_retail['CustomerID'].median()
#online_retail['CustomerID'].fillna(median, inplace=True)
#print(online_retail)
#print(online_retail.head(1700))

#drop the missing  data
#clean=online_retail.dropna()
#print(clean)

#print(online_retail)

# Fill missing data

#fil=online_retail.fillna("india")
#print(fil.head())

# Droping unnecessary field (unwanted columns)

#to_drop = ['Country']
#online_retail.drop(to_drop, inplace=True, axis=1)
#print(online_retail)


# Identifying fields in data

#print(online_retail.get_dtype_counts())
#print(online_retail)

#regex = r'^(\d{4})'

#extr = online_retail['InvoiceDate'].str.extract(r'^(\d{4})', expand=False)
#print(extr.head())


# group by the Country
#countries = online_retail.groupby('Country').sum()
#print(countries)

countries = online_retail.groupby('Country').count()
print(countries)

# create the plot
countries['Quantity'].plot(kind='line')

# Set the title and labels
plt.xlabel('Country')
plt.ylabel('Quantity')
plt.title('10 Countries with most orders')

# show the plot
plt.show()










