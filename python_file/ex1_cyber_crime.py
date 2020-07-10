import pandas as pd



#import csv file

path='C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime.csv'

# Read the data set ( for std encoding we use latin1 )

cc = pd.read_csv(path, encoding = 'latin1')

#print data set

#print(cc)

#Display total rows and columns

#print(cc.shape)

# Display the dataset first five rows

#print(cc.head())
#print(cc.tail())
# Display the whole dataset records

#print(cc)

# Display the dataset information

#print(cc.info())

# Display the dataset single column value

#print(cc.YEAR)

# Display the dataset mean, medium and other values(AGREEGATION ON WHOLE DATA SET)
#print(cc.describe())
#print(cc.describe())
"""print("MEAN OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.mean())

print("MEDIAN OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.median())

print("MODE OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.mode())

print("MINIMUM OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.min())

print("MAXIMUM OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.max())

print("NO.OF ROWS OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.count())

print("SD OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.std())

print("Q1 OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.quantile([0.25]))

print("Q3 OF CYBER CRIME DATA SET")
print("----------------------------")
print(cc.quantile([0.75]))"""





#display count unique top freq(AGREEGATION ON PARTICULER COLUMN)
"""print(cc['STATE/UT'].describe())
print(cc['YEAR'].describe())
print(cc['Below 18 Years'].describe())
print(cc['Between 18-30 Years'].describe())
print(cc['Between 30-45 Years'].describe())
print(cc['Between 45-60 Years'].describe())
print(cc['Above 60 Years'].describe())
print(cc['Total'].describe())"""

#use mean,median.mode.Q1,Q2,Q3,min,max,Std  
"""print('Mean =',cc['Below 18 Years'].mean())
print('Q1 = ',cc['Below 18 Years'].quantile([0.25]))
print('Median / Q2 =',cc['Below 18 Years'].median())
print('Q3 = ',cc['Below 18 Years'].quantile([0.75]))
print('Mode =',cc['Below 18 Years'].mode())
print('Minimum =',cc['Below 18 Years'].min())
print('Maximum =',cc['Below 18 Years'].max())
print('Standerd Deviation =',cc['Below 18 Years'].std())
print('Total Rows =',cc['Below 18 Years'].count())"""




"""
# Total missing values for each feature
print(df.isnull())
#sum of all null values
print(df.isnull().sum())"""



"""
#display the dataset columns

print(cc.columns)
# Handling missing data ( check for null value)
print(cc.isnull())
print(cc.isnull().sum())
print(cc['STATE/UT'].isnull())
print(cc.isnull())
print(cc['CRIME HEAD'].isnull().sum())
print(cc.isnull())
print(cc['YEAR'].isnull())
print(cc.isnull())
print(cc['Below 18 Years'].isnull().sum())
print(cc.isnull())
print(cc['Between 18-30 Years'].isnull())
print(cc.isnull())
print(cc['Between 30-45 Years'].isnull())
print(cc.isnull())
print(cc['Between 45-60 Years'].isnull())
print(cc.isnull())
print(cc['Above 60 Years'].isnull())
print(cc.isnull())
print(cc['Total'].isnull())
"""
 
"""
#for finding missing data

print(cc['Below 18 Years'].isnull().sum())
print(cc.isnull())
"""

"""

# Replace missing values with a number
cc['Total'].fillna('100', inplace=True)
print(cc)
"""

"""
#drop the missing  data
clean=cc.dropna()
print(clean)
"""

"""
# Droping unnecessary field (unwanted columns)

#to_drop = ['Total']
#cc.drop(to_drop, inplace=True, axis=1)
#print(cc)
"""





#group by

year = cc.groupby('YEAR').sum()
print(year)


"""
#Asecnding order
Asending=cc.sort_values(by ='STATE/UT',ascending=True)[1:11]
print(Asending)

#Descending order
stat=cc.sort_values(by ='STATE/UT',ascending=False)[1:11]
print(stat)

"""
"""
#lower
#cc["STATE/UT"]=cc["STATE/UT"].str.lower()
#print(cc)

#Upper
#cc["STATE/UT"]=cc["STATE/UT"].str.upper()
#print(cc)

"""

