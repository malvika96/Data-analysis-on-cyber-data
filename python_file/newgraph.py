import pandas as pd
import matplotlib.pyplot as plt


table = pd.read_csv("C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime2.csv")
df = pd.DataFrame(table,columns=['STATE/UT','CRIME HEAD','YEAR','Below 18 Years','Between 18-30 Years','Between 30-45 Years','Between 45-60 Years','Above 60 Years','Total'])
#df.plot.bar()
#df.hist()


"""
gapminder_2007 = df[df['YEAR']==2008]
gapminder_2007.shape
gapminder_2007.boxplot(by='Below 18 Years', column=['Total'],  grid=False)
plt.xlabel('Crimes')
plt.ylabel('Total')

#gapminder_2007 = df[df['YEAR']==2008]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 18-30 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2008]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 30-45 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2008]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 45-60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2008]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Above 60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2008]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Total', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')

"""

"""
#boxplot graphs
#year 2009

#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Below 18 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 18-30 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 30-45 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 45-60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Above 60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2009]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Total', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')

"""
#boxplot graphs
#year 2010
"""
apminder_2007 = df[df['YEAR']==2010]
gapminder_2007.shape
gapminder_2007.boxplot(by='Below 18 Years', column=['Total'],  grid=False)
plt.xlabel('Crimes')
plt.ylabel('Total')
"""

#gapminder_2007 = df[df['YEAR']==2010]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 18-30 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2010]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 30-45 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2010]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 45-60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2010]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Above 60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2010]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Total', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')



#boxplot graphs
#year 2011

#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Below 18 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 18-30 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 30-45 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 45-60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Above 60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2011]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Total', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')



#boxplot graphs
#year 2012

#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Below 18 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 18-30 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 30-45 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Between 45-60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Above 60 Years', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')


#gapminder_2007 = df[df['YEAR']==2012]
#gapminder_2007.shape
#gapminder_2007.boxplot(by='Total', column=['Total'],  grid=False)
#plt.xlabel('Crimes')
#plt.ylabel('Total')

"""



#Scatter plot Graphs
#year = df['Below 18 Years']
#sea_levels = df['STATE/UT']
#plt.scatter(year, sea_levels, edgecolors='r')
#plt.xlabel('Years')
#plt.ylabel('State')
#plt.title('Crime rate below 18 years')
#plt.show()

#year = df['Between 18-30 Years']
#sea_levels = df['STATE/UT']
#plt.scatter(year, sea_levels, edgecolors='r')
#plt.xlabel('Years')
#plt.ylabel('State')
#plt.title('Crime rate Between 18-30 years')
#plt.show()

#year = df['Between 30-45 Years']
#sea_levels = df['STATE/UT']
#plt.scatter(year, sea_levels, edgecolors='r')
#plt.xlabel('Years')
#plt.ylabel('State')
#plt.title('Crime rate between 30-45 years')
#plt.show()

#year = df['Between 45-60 Years']
#sea_levels = df['STATE/UT']
#plt.scatter(year, sea_levels, edgecolors='r')
#plt.xlabel('Years')
#plt.ylabel('State')
#plt.title('Crime rate between 45-60 years')
#plt.show()

#year = df['Above 60 Years']
#sea_levels = df['STATE/UT']
#plt.scatter(year, sea_levels, edgecolors='r')
#plt.xlabel('Years')
#plt.ylabel('State')
#plt.title('Crime rate Above 60 Years')
#plt.show()
"""

"""
year = df['Total']
sea_levels = df['STATE/UT']
plt.scatter(year, sea_levels, edgecolors='r')
plt.xlabel('Total')
plt.ylabel('State')
plt.title(' Total Crime ratio in each state of India')
#plt.show()
"""



"""
#state vs total
plt.bar(df['STATE/UT'], df['Total'])
plt.title("The total crime ratio in state of india")
plt.xlabel("state") 
plt.ylabel("total")
"""

"""
#age vs year
plt.bar(df['Below 18 Years'], df['YEAR'])
plt.bar(df['Between 18-30 Years'], df['YEAR'])
plt.bar(df['Between 30-45 Years'], df['YEAR'])
plt.bar(df['Between 45-60 Years'], df['YEAR'])
plt.bar(df['Above 60 Years'], df['YEAR'])
plt.title("commper in which year crime ratio age wise")
plt.xlabel("AGE") 
plt.ylabel("YEAR")
"""
"""
#year vs total
plt.bar(df['YEAR'], df['Total'])
plt.title("Total crime ratio in year")
plt.xlabel("Year") 
plt.ylabel("Total")
"""

"""
#crime head vs age
plt.xlabel("CRIME HEAD") 
plt.ylabel("AGE")
plt.title("Crime ratio of below 18 years as crime head in India ")
data=df['CRIME HEAD']
data1=df['Below 18 Years']
plt.pie(data1,labels=data,autopct ='% 1.1f %%', shadow = True) 
"""
plt.show()
