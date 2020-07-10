import pandas as pd
import matplotlib.pyplot as plt


table = pd.read_csv("C://Users//MALVIKA//Desktop//18mcl2//Project_datascience/cyber_Crime2.csv")
df = pd.DataFrame(table,columns=['STATE/UT','CRIME HEAD','YEAR','Below 18 Years',
'Between 18-30 Years','Between 30-45 Years','Between 45-60 Years','Above 60 Years','Total'])

year = df['YEAR']
age = df['Below 18 Years']
plt.scatter(year, age, edgecolors='r')
plt.xlabel('YEAR')
plt.ylabel('AGE')
plt.title('CRIME RATIO AGE WISE PER YEAR IN INDIA')
plt.show()





"""
plt.title("CRIME RATIO OF BELOW 18 YEARS PER YEAR IN INDIA")
data=df['YEAR']
data1=df['Below 18 Years']
plt.pie(data1,labels=data,autopct ='% 1.1f %%', shadow = True) 
plt.show()
"""

"""
plt.bar(df['Below 18 Years'], df['CRIME HEAD'])
#plt.bar(df['Between 18-30 Years'], df['CRIME HEAD'])
#plt.bar(df['Between 30-45 Years'], df['CRIME HEAD'])
#plt.bar(df['Between 45-60 Years'], df['CRIME HEAD'])
#plt.bar(df['Above 60 Years'], df['CRIME HEAD'])
#plt.bar(df['Total'], df['CRIME HEAD'])
plt.xlabel("AGE") 
plt.ylabel("CRIME HEAD")
plt.title('CRIME RATIO AGE WISE ON CRIME HEAD')
plt.show()
"""


"""
df.boxplot(column=['Below 18 Years'])
plt.xlabel('AGE')
plt.ylabel('CRIME RATIO')
plt.title('CRIME RATIO AGE WISE')
plt.show()

"""

"""
#df.hist(column=['YEAR','Total'])
df.hist(column=['YEAR','Below 18 Years'])
#df.hist(column=['YEAR','Between 18-30 Years'])
#df.hist(column=['YEAR','Between 30-45 Years'])
#df.hist(column=['YEAR','Between 45-60 Years'])
#df.hist(column=['YEAR','Above 60 Years'])
plt.xlabel('YEAR')
plt.ylabel('TOTAL CRIME')
plt.title('TOTAL CRIME RATIO AGE WISE PER YEAR')
plt.show()


df=pd.read_csv("C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime.csv")
df.plot()
df.plot(kind='scatter',x='YEAR',y='Below 18 Years')
df.plot(kind='density')

"""

#crime vs age graph

#year vs crime
#plt.bar(df['YEAR'], df['CRIME HEAD'])
#plt.xlabel("year") 
#plt.ylabel("crime head")

#state vs crime
#plt.bar(df['STATE/UT'], df['CRIME HEAD'])
#plt.xlabel("state") 
#plt.ylabel("crime head")

#state vs total
#plt.bar(df['STATE/UT'], df['Total'])
#plt.xlabel("state") 
#plt.ylabel("total")

#age vs total
#plt.bar(df['Below 18 Years'], df['Total'])
#plt.bar(df['Between 18-30 Years'], df['Total'])
#plt.bar(df['Between 30-45 Years'], df['Total'])
#plt.bar(df['Between 45-60 Years'], df['Total'])
#plt.bar(df[Above 60 Years'], df['Total'])
#plt.xlabel("Ages") 
#plt.ylabel("Total")

#year vs total
#plt.bar(df['YEAR'], df['Total'])
#plt.xlabel("Year") 
#plt.ylabel("Total")


