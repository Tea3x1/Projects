#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset (Gapminder World)
# 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href ="#Functions">Functions</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#Question 1">Question 1:Which is the most and least country in Murder rate?</a></li>
# <li><a href="#Question 2">Question 2 : Which is the most and least country in Population?</a></li>
# <li><a href="#Question 3">Question 3 : Which country has the most and least GDP Rate?</a></li>
# <li><a href="#Question 4">Question 4 : Which country has the most and least Income Rate?</a></li>
# <li><a href="#Question 5">Question 5 : Which country has the most and least Unemployment Rate?</a></li>
# <li><a href="#Question 6">Question 6 : Does Unemployment rate have an effect on Murder rate?</a></li>
# <li><a href="#Question 7">Question 7 : Does increase in Income rate will lead to decrease the Murder rate?</a></li>
# <li><a href="#Question 8">Question 8: Does the increase in Population effect the Unemployment Rate?</a></li>
# <li><a href="#Question 9">Question 9: Does the increase in Murder rate effect the Economy?</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# <li><a href="#limitations">Limitations</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# #### We will explore these indicators in this data investigation ...
# >Population rate ---> The human population explosion not only affects humans but also our environment and wildlife.As more population requires more resources, deforestation is happening at a faster rate which takes away the homes of these animals. Similarly, their habitat is being destroyed owing to human activities.the increased need calls for faster rates of industrialization. These industries pollute our water and lands, harming and degrading our quality of life.
# 
# >Crime Rate ---> Murder is the unlawful killing of another human without justification or valid excuse, especially the unlawful killing of another human with malice aforethought. , In this file we will explore the murder rate in the whole world .. To calculate the Murder ratio we have to divide the murder rate on the country population ...
# 
# >GDP Growth Rate ---> Economics is a social science devoted to the study of how people and societies get what they need and want. In this file , We will explore the world economic growth since 1990 till 2016 ...
# 
# >Unemployemnt rate ---->Unemployment is a very serious issue not only in India but in the whole world. There are hundreds and thousands of people out there who do not have employment.It will lead to an increase in poverty, an increase in crime rate, exploitation of labor, political instability, mental health, and loss of skills. As a result, all this will eventually lead to the demise of the nation.
# 
# > income rate for per person ---> For individuals and businesses, income generally means the value or amount that they receive for their labor and products.Individuals generally consider their gross income to equal the total of their earnings in the form of wages and salaries, the return on their investments and sales of property, and other receipts. Their net income is composed of their gross income reduced by costs incurred in producing the income.

# In[406]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'notebook')


# <a id='wrangling'></a>
# ## Data Wrangling

# In[407]:


df_GDP = pd.read_csv("Project2/GDP_growth_rate.csv")
df_Murder = pd.read_csv("Project2/murder_total_deaths.csv")
df_Population = pd.read_csv("Project2/population_total.csv")
df_Income = pd.read_csv("Project2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
df_Unemployment = pd.read_csv("Project2/Unemployment_rate.csv")


# ### Exploring the collected data ...

# In[408]:


df_GDP.head()


# In[409]:


df_Murder.head()


# In[410]:


df_Population.head()


# In[411]:


df_Income.head()


# In[412]:


df_Unemployment.head()


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# <a id='Functions'></a>
# ## Functions

# #### This Function replace K , M , B With thousand , million , billion.. as numbers ....

# In[414]:


def replacing(df):
    #First i replaced all K, M , B with empty space , Then i extracted all the K, M , B to its amount in numbers and multiply it in the number that had them..
    for values in df.columns[1:]:
        df[values] = df[values].replace(r'[kMB]+$', '', regex=True).astype(float) * df[values].str.extract(r'[\d\.]+([kMB]+)', expand=False).fillna(1).replace(['k','M',"B"], [10**3, 10**6, 10**9]).astype(int)
    
    return df


# #### Droping all years except years from 1990 till 2016 ..

# In[415]:


years = df_Income.columns[df_Income.columns.get_loc("1990"):df_Income.columns.get_loc("2016")+1]
def filtering_years(df):
    for year in df.columns:
        if year not in years and year not in ["country", "Country"]:
            df.drop(year, axis=1, inplace=True)
    
    return df


# #### This function will return only the data in 2000, 2005, 2010 and 2016 , it will help me in visualizing my data since there are alot of years ...

# In[416]:


ye2 = [2000 , 2005 , 2010 , 2016]
def Comparing(df):
    new_df = df[(df.index == "2000") | (df.index == "2005") | (df.index == "2010") | (df.index == "2016")]
            
    return new_df


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ### Data Cleaning ..

# #### Checking for Nan Values in each data ..

# In[417]:


sum(df_Population.isnull().sum())


# In[418]:


sum(df_Income.isnull().sum())


# In[419]:


sum(df_Murder.isnull().sum())


# In[420]:


sum(df_GDP.isnull().sum())


# In[421]:


sum(df_Unemployment.isnull().sum())


# #### Removing NaN values from Unemployment and GDP dataframes..

# In[422]:


df_GDP.fillna(0,inplace=True)


# In[423]:


df_Unemployment.fillna(0, inplace=True)


# #### Rechecking forr Nan Values ..

# In[424]:


sum(df_GDP.isnull().sum())


# In[425]:


sum(df_Unemployment.isnull().sum())


# #### Droping all the other years except years from 1990 till 2016 ..

# In[426]:


filtering_years(df_GDP)


# In[427]:


filtering_years(df_Unemployment)


# In[428]:


filtering_years(df_Population)


# In[429]:


filtering_years(df_Murder)


# In[430]:


filtering_years(df_Income)


# #### Replacing K , M , B with numbers ...

# In[431]:


replacing(df_Income)


# In[432]:


replacing(df_Murder)


# In[433]:


replacing(df_Population)


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ## Joining Total murder data with population data to calculate the murder rate ...

# #### Here i joined the total murder data to the right side of the population data and i marked its years by  adding _Murder_counts to them .. in order to be able to calculate the murder ratio .... Murder ratio = total murder / population * 100k per population ...

# In[434]:


murder_ratio = df_Population.join(df_Murder,rsuffix="_Murder")


# In[435]:


murder_ratio


# In[436]:


# Checking the dimension of the murder ratio data... 
murder_ratio.shape


# In[437]:


#Putting the countries in the population data in population variable,  and putting the countries in the total murder data to the murder variable   ...
population = murder_ratio["country"].sort_values().values


# In[438]:


murder = murder_ratio["country_Murder"].sort_values().values


# In[439]:


population


# In[440]:


murder


# In[441]:


# I used for loop to go through the countries in the population list , then if this country not in the countries murder list . i will remove it from the data ...
for country in population:
    if country not in murder:
        population[population != country]

# Using the countries in the total murder as an index for the data..
murder_ratio.set_index("country_Murder", inplace = True)


# In[442]:


# removing the column that have population countries ...
murder_ratio.drop(columns="country",inplace=True)


# In[443]:


#Reseting the index to use numbers instead of the Countries in the total murder ...
murder_ratio.reset_index(inplace=True)


# In[444]:


# Getting the Years that have Murder_counts in it and seperate it from the population years...
murder_columns_list = murder_ratio.columns

murder_years = murder_ratio.columns[murder_columns_list.get_indexer(["1990_Murder"])[0]:]

population_years = murder_ratio.columns[1:murder_columns_list.get_indexer(["1990_Murder"])[0]]


# In[445]:


population_years


# In[446]:


# Comparing the length of two list to make sure that we have the same years ..
len(population_years)


# In[447]:


len(murder_years)


# In[448]:


# Getting the Murder ratio by dividing the total murder on the population number then multiplaying it with 100k to get it per 100k population ...Then i add the result in a new Columns and label them with the number of the year + Per 100k ..
for i in range(0,len(population_years)):
    murder_ratio["{}_Per 100k".format(population_years[i])] = (murder_ratio[murder_years[i]] / murder_ratio[population_years[i]]) * 100000


# In[449]:


murder_ratio


# In[450]:


#Removing the other years coulmns that doesnt have Per 100k since we only need the raito..
for i in range(0,len(population_years)):
    murder_ratio.drop(population_years[i], axis=1,inplace=True)
    murder_ratio.drop(murder_years[i], axis=1,inplace=True)


# In[451]:


murder_ratio


# In[452]:


# Changing country_Murder_counts to Country since this is the only column that have countries in it ....
murder_ratio.columns = murder_ratio.columns.str.replace(r'_[^_]*$', '',regex=True)
                        


# In[453]:


murder_ratio


# #### Removing NaN rows in The DataFrame...

# In[454]:


murder_ratio = murder_ratio[0:194]


# #### Checking if There is any NaN Values..

# In[455]:


sum(murder_ratio.isnull().sum())


# In[456]:


murder_ratio


# In[457]:


# new_murder = countries(murder_ratio)


# #### Making the Country column my indeces ...

# In[458]:


murder_ratio.set_index("country", inplace = True)


# In[459]:


murder_ratio = murder_ratio.T


# In[460]:


murder_ratio.columns.rename(name="Years",inplace=True) # --> Renaming the country name to Years...


# In[463]:


murder_ratio


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ### Working on the GDP Data ... 

# #### Making the Country column my indeces ...

# In[466]:


df_GDP.set_index("Country",inplace=True)


# In[467]:


df_GDP


# #### Transposing the columns with the indeces

# In[468]:


df_GDP = df_GDP.T


# In[469]:


df_GDP


# In[470]:


df_GDP.columns.rename(name="Years",inplace=True) # --> Renaming the country name to Years...


# In[473]:


df_GDP


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ### Working on the Income Data ... 

# In[476]:


df_Income.set_index("country",inplace=True) # Making the Country column my indeces ...


# In[477]:


df_Income


# In[478]:


df_Income = df_Income.T # Transposing the columns with the indeces


# In[479]:


df_Income


# In[480]:


df_Income.columns.rename(name="Years",inplace=True)


# In[547]:


df_Income


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###
# 

# ### Working on UnEmployment Dataframe ...

# In[486]:


df_Unemployment.set_index("Country",inplace=True)


# In[487]:


df_Unemployment = df_Unemployment.T


# In[488]:


df_Unemployment.columns.rename(name="Years",inplace=True)


# In[491]:


df_Unemployment


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###
# 

# In[492]:


df_Population.set_index("country", inplace = True)


# In[493]:


df_Population = df_Population.T


# In[494]:


df_Population.columns.rename(name="Years",inplace=True)


# In[497]:


df_Population


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###
# 

# <a id='eda'></a>
# ## Exploratory Data Analysis

# #### I Found it hard to compare the data bcz its big ... So i decided to visualize few countries alone like (Russia , Egypt , Afghanistan, China, Japan, and United States ..

#    ### ----------------------------------------------------------------------------------------------- #

# ## Murder Rate Data ..

# ### Egypt 

# In[498]:


plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_Egypt_Murder.index, ymin=0, ymax=comparing_Egypt_Murder.values,label='Egypt',color="#66995A")
for x, y in zip(comparing_Egypt_Murder.index, comparing_Egypt_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'red' if y > 1.2 else '#098003', 'size':14})
plt.plot(comparing_Egypt_Murder.index, comparing_Egypt_Murder.values,'o--', color='#1A1429', alpha=0.5)
# Decorations    
# plt.yticks(df.index, df.cars, fontsize=12)
# plt.xlim(-2.5, 2.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("Egypt Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper left",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[499]:


Average_Egypt_Murder = (0.83 + 1.04 + 1.3 + 1.33)/ 4
Average_Egypt_Murder


# #### As we can see from the chart that murder rate in Egypt increases with an average of 1.125 every 5 Years ....

# #### Exploring more details ..

# In[500]:


murder_ratio.Egypt.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Japan 

# In[501]:


comparing_Japan_Murder = Comparing(murder_ratio.Japan)
plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_Japan_Murder.index, ymin=0, ymax=comparing_Japan_Murder.values,label='Japan',color="#4D2403")
for x, y in zip(comparing_Japan_Murder.index, comparing_Japan_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#c91a22' if y > 2.5 else '#098003', 'size':14})
plt.plot(comparing_Japan_Murder.index, comparing_Japan_Murder.values,'o--', color='#BA631C', alpha=0.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("Japan Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper right",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[502]:


Average_Japan_Murder = (3.5 + 2.79 + 2.13 + 1.64)/ 4
Average_Japan_Murder


# #### As we can see from the chart that murder rate in Japan decreases with an average of 2.515 every 5 Years ....

# #### Exploring more details ..

# In[503]:


murder_ratio.Japan.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Russia 

# In[504]:


comparing_Russia_Murder = Comparing(murder_ratio.Russia)
plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_Russia_Murder.index, ymin=0, ymax=comparing_Russia_Murder.values,label='Russia',color="#6010BB")
for x, y in zip(comparing_Russia_Murder.index, comparing_Russia_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#c91a22' if y > 150 else '#098003', 'size':14})
plt.plot(comparing_Russia_Murder.index, comparing_Russia_Murder.values,'o--', color='#63B00C', alpha=0.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("Russia Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper right",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[505]:


Average_Russia_Murder = (210.41 + 193.93 + 136.59 + 124.24)/ 4
Average_Russia_Murder


# #### As we can see from the chart that murder rate in Russia increases with an average of 166.292 every 5 Years ....

# #### Exploring more details ..

# In[506]:


murder_ratio.Russia.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Afghanistan 

# In[507]:


comparing_Afghanistan_Murder = Comparing(murder_ratio.Afghanistan)
plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_Afghanistan_Murder.index, ymin=0, ymax=comparing_Afghanistan_Murder.values,label='Afghanistan',color="#36110A")
for x, y in zip(comparing_Afghanistan_Murder.index, comparing_Afghanistan_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#c91a22' if y > 17.26 else '#098003', 'size':14})
plt.plot(comparing_Afghanistan_Murder.index, comparing_Afghanistan_Murder.values,'o--', color='#6B1F15', alpha=0.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("Afghanistan Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper right",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[508]:


Average_Afghanistan_Murder = (17.26 + 18.48 + 16.92 + 17.71)/ 4
Average_Afghanistan_Murder


# #### As we can see from the chart that murder rate in Afghanistan increases and decreases with an average of 17.5925 every 5 Years ....

# #### Exploring more details ..

# In[509]:


murder_ratio.Afghanistan.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### United States 

# In[510]:


comparing_USA_Murder = Comparing(murder_ratio["United States"])
plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_USA_Murder.index, ymin=0, ymax=comparing_USA_Murder.values,label='United States',color="#36110A")
for x, y in zip(comparing_USA_Murder.index, comparing_USA_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#c91a22' if y > 60 else '#098003', 'size':14})
plt.plot(comparing_USA_Murder.index, comparing_USA_Murder.values,'o--', color='#6B1F15', alpha=0.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("United States Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper right",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[511]:


Average_USA_Murder = (76.79 + 67.15 + 54.01 + 46.21)/ 4
Average_USA_Murder


# #### As we can see from the chart that murder rate in USA decreases with an average of 61.04 every 5 Years ....

# #### Exploring more details ..

# In[512]:


murder_ratio["United States"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### China 

# In[513]:


comparing_China_Murder = Comparing(murder_ratio.China)
plt.figure(figsize=(15,10), dpi= 65)
plt.vlines(x=comparing_China_Murder.index, ymin=0, ymax=comparing_China_Murder.values,label='China',color="#36110A")
for x, y in zip(comparing_China_Murder.index, comparing_China_Murder.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#c91a22' if y > 150 else '#098003', 'size':14})
plt.plot(comparing_China_Murder.index, comparing_China_Murder.values,'o--', color='#6B1F15', alpha=0.5)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
title_size = 18
plt.title("China Murder Rate" ,fontsize=title_size)
plt.legend(loc="upper right",fontsize= 15)
plt.ylabel("Rate",fontsize=title_size)
plt.xlabel("Years", fontsize=title_size)
plt.tick_params(labelsize=16,length=0)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# In[514]:


Average_China_Murder = (283.23 + 177.4 + 115.27 + 78.24)/ 4
Average_China_Murder


# #### As we can see from the chart that murder rate in China decreases with an average of 163.535 every 5 Years ....

# #### Exploring more details ..

# In[515]:


murder_ratio.China.describe()


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# <a id='Question 1'></a>
# ### Question 1 : Which country has the most and least Murder rate?

# ### Answer :

# #### Calulating the countries that has the most and least Murder rate ... 

# In[516]:


df_Murder.set_index("country", inplace = True)


# In[517]:


df_Murder = df_Murder.T


# In[518]:


df_Murder.columns.rename(name="Years",inplace=True)


# In[519]:


murder = {}
for country in df_Murder.columns:
    murder[df_Murder[country].mean()] = country


# ### Which Country has the most murder Rate?

# In[520]:


print("The country with the most Murder Rate is {} with an average of --> {} ....".format(murder[max(murder.keys())],max(murder.keys())))


# ### Which Country has the Least murder Rate?

# In[521]:


print("The country with the Least Murder Rate is {} with an average of --> {} ....".format(murder[min(murder.keys())],min(murder.keys())))


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ## Population rate

#    ### ----------------------------------------------------------------------------------------------- #
# ### Egypt 

# In[522]:


comparing = df_Population[(df_Population.index == "2000") | (df_Population.index == "2005") | (df_Population.index == "2010") | (df_Population.index == "2016")]

fig,ax = plt.subplots(figsize=(15,10),dpi=70)
splot = sns.barplot(x=ye2,y=comparing.Egypt,data=comparing,ci=95,ax=ax,palette = "viridis")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
        
title_size = 18
ax.set_title("Egypt Population" ,fontsize=title_size)
ax.set_ylabel("Count",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[523]:


Egyption_Population = 94400000 - 68800000
Egyption_Population


# #### As we can see from the chart that Egypt population has increased 25M person in only 16 years...

# In[524]:


comparing.Egypt.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Russia 

# In[525]:


fig,ax = plt.subplots(figsize=(15,10),dpi=70)
splot = sns.barplot(x=ye2,y=comparing.Russia,data=df_Population,ci=95,ax=ax,palette = "mako")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
        
title_size = 18
ax.set_title("Russia Population" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[526]:


Russia_Population = 14600000 - 14500000
Russia_Population


# #### As we can see from the chart that Russia population has decreased 100k person in 16 years...

# #### Exploring more details ..

# In[527]:


comparing.Russia.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### China 

# In[528]:


fig,ax = plt.subplots(figsize=(15,10),dpi=70)
splot = sns.barplot(x=ye2,y=comparing.China,data=df_Population,ci=95,ax=ax,palette = "cubehelix")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
        
title_size = 18
ax.set_title("China Population" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[529]:


China_Population = 1410000000 - 1290000000
China_Population


# #### As we can see from the chart that China population has increased 120M person in only 16 years...

# #### Exploring more details ..

# In[530]:


comparing.China.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Japan 

# In[531]:


fig,ax = plt.subplots(figsize=(15,10),dpi=70)
splot = sns.barplot(x=ye2,y=comparing.Japan,data=df_Population,ci=95,ax=ax,palette = "rocket_r")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
        
title_size = 18
ax.set_title("Japan Population" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[532]:


Japan_Population = 129000000 - 128000000
Japan_Population


# #### As we can see from the chart that Japan population has increased in 2010 with 1M person but decreased in 2016 to be same as 2000 population which is 128M person...

# #### Exploring more details ..

# In[533]:


comparing.Japan.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### United States 

# In[534]:


fig,ax = plt.subplots(figsize=(15,10),dpi=70)
splot = sns.barplot(x=ye2,y=comparing["United States"],data=df_Population,ci=95,ax=ax,palette = "RdYlGn")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
        
title_size = 18
ax.set_title("United States Population" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[535]:


USA_Population = 323000000 - 282000000
USA_Population


# #### As we can see from the chart that USA population has increased 41M person in only 16 years...

# #### Exploring more details ..

# In[536]:


comparing["United States"].describe()


# In[537]:


comparing_Afghanistan_Population.values


#    ### ----------------------------------------------------------------------------------------------- #
# ### Afghanistan 

# In[538]:


fig,ax = plt.subplots(figsize=(15,10),dpi=70)
comparing_Afghanistan_Population = Comparing(df_Population.Afghanistan)
splot = sns.barplot(x=ye2,y=comparing_Afghanistan_Population,data=df_Population,ci=95,ax=ax,palette = "magma")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), ".1f"), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')

for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - 0.1

        # we change the bar width
        patch.set_width(.1)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)
        
title_size = 18
ax.set_title("Afghanistan Population" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# In[539]:


Afghanistan_Population = 354000000 - 208000000
Afghanistan_Population


# #### As we can see from the chart that Egypt population has increased 146M person in only 16 years...

# #### Exploring more details ..

# In[540]:


comparing.Afghanistan.describe()


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# <a id='Question 2'></a>
# ### Question 2 : Which is the most and least country in Population?

# ## Answer:

# #### Calulating the countries that has the most and least population rate 

# In[541]:


population = {}
for country in df_Population.columns:
    population[df_Population[country].mean()] = country


# ### Which country has the most population  ?

# In[542]:


print("The country with the most Population Rate is {} with an average of --> {} ....".format(population[max(population.keys())],max(population.keys())))


# ### Which country has the least population ?

# In[543]:


print("The country with the most Population Rate is {} with an average of --> {} ....".format(population[min(population.keys())],min(population.keys())))


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ## GDP Data

# In[544]:


plt.style.use('seaborn-dark')
comparing_Egypt_GDP = Comparing(df_GDP.Egypt)
comparing_Russia_GDP = Comparing(df_GDP.Russia)
comparing_China_GDP = Comparing(df_GDP.China)
comparing_Afghanistan_GDP = Comparing(df_GDP.Afghanistan)
comparing_Japan_GDP = Comparing(df_GDP.Japan)
comparing_USA_GDP = Comparing(df_GDP["United States"])

fig, ax = plt.subplots(figsize = (15,10),dpi=65)

a = ax.plot(comparing_Egypt_GDP.index, comparing_Egypt_GDP.values, 'o-',color='#7f6d5f', label='Egypt')
ax.plot(comparing_China_GDP.index, comparing_China_GDP.values, 'o-', color='#557f2d', label='China')
ax.plot(comparing_Russia_GDP.index, comparing_Russia_GDP.values,'D-',color='#2d7f5e',label='Russia')
ax.plot(comparing_Japan_GDP.index, comparing_Japan_GDP.values, 'o-',color='#120603',label='Japan')
ax.plot(comparing_Afghanistan_GDP.index, comparing_Afghanistan_GDP.values, 'o-',color='#c912c6',label='Afghanistan')
ax.plot(comparing_USA_GDP.index, comparing_USA_GDP.values, 'o-',color='#DE5833',label='United States')
ax.set_title('GDP Growth for group of countries')
ax.set_xlabel('Years')
ax.set_ylabel('Ratio')
plt.legend()
plt.grid(axis = 'x', linestyle=':', alpha=1,color = 'black')
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that Afghanistan GDP Increased from 0% in 2000 to 14.8% in 2010 then decreased to 2.4% in 2016 .. 
# #### While Russia and Japan had a 10% and 2.9% in their GDP in 2000 but decreased alot in 2016 with a 0.1 % for Russia and 0.4 for Japan. ...
# #### Egypt had more increase in GDP than USA by 6.2% to 4.1% in 2000 and same for 2016 Egypt Had 4.3% Increase while USA had 1.8% increase .
# #### But for China it started with 8.8% increase in 2000 but decreased to 7% in 2016 ...

#    ### ----------------------------------------------------------------------------------------------- #
# 

# ### Egypt 

# In[545]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_Egypt_GDP.index,y=comparing_Egypt_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "viridis")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')
title_size = 18
ax.set_title("Egypt GDP Growth Rate" ,fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is a decrease in Egypt GDP since 2000 till 2016 by 2.1% ..

# #### Exploring more details ..

# In[548]:


df_GDP.Egypt.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Russia 

# In[623]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_Russia_GDP.index,y=comparing_Russia_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "mako")
for p in splot.patches:
    if p.get_height() > 0: # -- > i used if statments bcz when i try to use annotators , there is some countries that have negative values , so the position of the value gets in the bar.. 
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 : # --> i had to seperate the positive values from the negative values and give each ot them a different axis...
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), # ---> Negative y axis since its a negative value ...
                       textcoords = 'offset points')
    
ax.set_title("Russia GDP Growth Rate",fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is a decrease in Russia GDP since 2000 till 2016 by 9.8% ..

# #### Exploring more details ..

# In[549]:


df_GDP.Russia.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### United States 

# In[624]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_USA_GDP.index,y=comparing_USA_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "RdYlGn")
for p in splot.patches:
    if p.get_height() > 0:
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 :
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), 
                       textcoords = 'offset points')
    
ax.set_title("United States GDP Growth Rate",fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is a decrease in USA GDP since 2000 till 2016 by 3.6% ..

# #### Exploring more details ..

# In[550]:


df_GDP["United States"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Afghanistan 

# In[625]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_Afghanistan_GDP.index,y=comparing_Afghanistan_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "viridis")
for p in splot.patches:
    if p.get_height() > 0:
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 :
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), 
                       textcoords = 'offset points')
    
ax.set_title("Afghanistan GDP Growth Rate",fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is an increase in Afghanistan GDP since 2000 till 2016 by 2.3% ..

# #### Exploring more details ..

# In[551]:


df_GDP.Afghanistan.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### China 

# In[626]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_China_GDP.index,y=comparing_China_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "cubehelix")
for p in splot.patches:
    if p.get_height() > 0:
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 :
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), 
                       textcoords = 'offset points')
    
ax.set_title("China GDP Growth Rate",fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is a decrease in China GDP since 2000 till 2016 by 2.3% ..

# #### Exploring more details ..

# In[552]:


df_GDP.China.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Japan 

# In[627]:


fig,ax = plt.subplots(figsize=(10,7),dpi=65)
splot = sns.barplot(x=comparing_Japan_GDP.index,y=comparing_Japan_GDP.values,data=df_GDP,ci=95,ax=ax,palette = "rocket_r")
for p in splot.patches:
    if p.get_height() > 0:
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, 9), 
                       textcoords = 'offset points')
    if p.get_height() < 0 :
        splot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       size=15,
                       xytext = (0, -11), 
                       textcoords = 'offset points')
ax.set_title("Japan GDP Growth Rate",fontsize=title_size)
ax.set_ylabel("Ratio",fontsize=title_size)
ax.tick_params(labelsize=16,length=0)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from the chart that there is a decrease in Japan GDP since 2000 till 2016 by 2% ..

# #### Exploring more details ..

# In[553]:


df_GDP.Japan.describe()


#  ### ------------------------------------------------------------------------ ###

# <a id='Question 3'></a>
# ### Question 3 : Which country has the most and least GDP Rate?

# ## Answer:

# In[559]:


economy = {}
for country in df_GDP.columns[1:]:
    economy[df_GDP[country].mean()] = country


# ### Which country has the most GDP growth?

# In[560]:


print("The country with the most economy Growth is {} with an average of --> {} ....".format(economy[max(economy.keys())],max(economy.keys())))


# ### Which country has the least GDP growth ?

# In[561]:


print("The country with the least Growth is {} with an average of --> {} ....".format(economy[min(economy.keys())],min(economy.keys())))


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###

# ## Income Data 

# In[577]:


plt.figure(figsize=(15,10),dpi= 65)
comparing_Egypt_Income = Comparing(df_Income.Egypt)
comparing_Russia_Income = Comparing(df_Income.Russia)
comparing_China_Income = Comparing(df_Income.China)
comparing_Afghanistan_Income = Comparing(df_Income.Afghanistan)
comparing_Japan_Income = Comparing(df_Income.Japan)
comparing_USA_Income = Comparing(df_Income["United States"])

plt.step(comparing_Egypt_Income.index, comparing_Egypt_Income.values, label='Egypt')
plt.plot(comparing_Egypt_Income.index, comparing_Egypt_Income.values, 'o--', color='blue', alpha=0.3)
for x, y in zip(comparing_Egypt_Income.index, comparing_Egypt_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#1E5A6A', 'size':14})

plt.step(comparing_Russia_Income.index, comparing_Russia_Income.values, label='Russia')
plt.plot(comparing_Russia_Income.index, comparing_Russia_Income.values, 'o--', color='#a1a30b', alpha=0.3)
for x, y in zip(comparing_Russia_Income.index, comparing_Russia_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#7d870e', 'size':14})
    
plt.step(comparing_China_Income.index, comparing_China_Income.values, label='China')
plt.plot(comparing_China_Income.index, comparing_China_Income.values, 'o--', color='green', alpha=0.3)
for x, y in zip(comparing_China_Income.index, comparing_China_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#18540C', 'size':14})
    
plt.step(comparing_Japan_Income.index, comparing_Japan_Income.values, label='Japan')
plt.plot(comparing_Japan_Income.index, comparing_Japan_Income.values, 'o--', color='red', alpha=0.3)
for x, y in zip(comparing_Japan_Income.index, comparing_Japan_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#940025', 'size':14})
    
plt.step(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values, label='Afghanistan')
plt.plot(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values, 'o--', color='purple', alpha=0.3)
for x, y in zip(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#96005d', 'size':14})
    
plt.step(comparing_USA_Income.index, comparing_USA_Income.values, label='United States')
plt.plot(comparing_USA_Income.index, comparing_USA_Income.values, 'o--', color='grey', alpha=0.3)
for x, y in zip(comparing_USA_Income.index, comparing_USA_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#474747', 'size':14})
    
plt.title('Countries income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'y', linestyle=':', alpha=1,color = 'black')
plt.legend(fontsize = 14 , loc = "center left")
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : 
#    ####    Afghanistan income per person Increased from \\$578 in 2000 to \\$2060 in 2016.
#    ####    Russia income per person Increased from \\$14600 in 2000 to \\$25600 in 2016.
#    ####    Japan  income per person Increased from \\$35700 in 2000 to \\$40200 in 2016.
#    ####    Egypt income per person Increased from \\$7750 in 2000 to \\$10800 in 2016.
#    ####    USA income per person Increased from \\$50200 in 2000 to \\$59000 in 2016.
#    ####    China income per person Increased from \\$3450 in 2000 to \\$13500 in 2016.

#    ### ----------------------------------------------------------------------------------------------- #
# ### Egypt

# In[588]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_Egypt_Income.index, comparing_Egypt_Income.values, label='Egypt')
plt.plot(comparing_Egypt_Income.index, comparing_Egypt_Income.values, 'o--', color='blue', alpha=0.3)
for x, y in zip(comparing_Egypt_Income.index, comparing_Egypt_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#065266', 'size':14})
plt.title('Egypt income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'blue')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Egypt income per person Increased by \\$3050 in 16 years.
# 

# #### Exploring more details ..

# In[610]:


df_Income.Egypt.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Russia

# In[596]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_Russia_Income.index, comparing_Russia_Income.values, label='Russia', color = "#7d870e")
plt.plot(comparing_Russia_Income.index, comparing_Russia_Income.values, 'o--', color='#7d870e', alpha=0.3)
for x, y in zip(comparing_Russia_Income.index, comparing_Russia_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#596100', 'size':14})
plt.title('Russia income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#596100')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Russia income per person Increased by \\$11000 in 16 years.

# #### Exploring more details ..

# In[609]:


df_Income.Russia.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### China 

# In[598]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_China_Income.index, comparing_China_Income.values, label='China', color = "#18540C")
plt.plot(comparing_China_Income.index, comparing_China_Income.values, 'o--', color='green', alpha=0.3)
for x, y in zip(comparing_China_Income.index, comparing_China_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#18540C', 'size':14})
plt.title('China income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#18540C')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : China income per person Increased by \\$10050 in 16 years.

# #### Exploring more details ..

# In[608]:


df_Income.China.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Japan 

# In[601]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_Japan_Income.index, comparing_Japan_Income.values, label='Japan',color="#940025")
plt.plot(comparing_Japan_Income.index, comparing_Japan_Income.values, 'o--', color='red', alpha=0.3)
for x, y in zip(comparing_Japan_Income.index, comparing_Japan_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#940025', 'size':14})
plt.title('Japan income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#940025')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that :   Japan  income per person Increased by \\$4500 in 16 years.

# #### Exploring more details ..

# In[607]:


df_Income.Japan.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### United States 

# In[599]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_USA_Income.index, comparing_USA_Income.values, label='United States',color="#474747")
plt.plot(comparing_USA_Income.index, comparing_USA_Income.values, 'o--', color='grey', alpha=0.3)
for x, y in zip(comparing_USA_Income.index, comparing_USA_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#474747', 'size':14})
plt.title('United States income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#474747')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : USA income per person Increased by \\$8800 in 16 years.

# #### Exploring more details ..

# In[605]:


df_Income["United States"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Afghanistan

# In[603]:


plt.figure(figsize=(15,10),dpi= 65)
plt.step(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values, label='Afghanistan',color = '#96005d')
plt.plot(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values, 'o--', color='purple', alpha=0.3)
for x, y in zip(comparing_Afghanistan_Income.index, comparing_Afghanistan_Income.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#96005d', 'size':14})
plt.title('Afghanistan income Growth..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Income")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#96005d')
plt.legend(loc = "upper left", fontsize = 14)
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that :  Afghanistan income per person Increased by \\$1482 in 16 years.
# 

# #### Exploring more details ..

# In[606]:


df_Income.Afghanistan.describe()


# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='Question 4'></a>
# ### Question 4 : Which country has the most and least Income Rate?

# ## Answer

# #### Calulating the countries that has the most and least income rate ... 

# In[611]:


Income = {}
for country in df_Income.columns[1:]:
    Income[df_Income[country].mean()] = country


# ### Which country has the most income per person?

# In[614]:


print("The country with the most Income Rate is {} with an average of --> ${}  ....".format(Income[max(Income.keys())],max(Income.keys())))


# ### Which country has the least income per person?

# In[620]:


print("The country with the least Income Rate is {} with an average of --> ${} ....".format(Income[min(Income.keys())],min(Income.keys())))


# ## -------------------------------------------------------------------------------------------------------------------------- ###

# ## UnEmployment Ratio Data

# In[632]:


plt.figure(figsize=(15,10),dpi= 65)
comparing_Egypt_Unemployment = Comparing(df_Unemployment.Egypt)
comparing_Russia_Unemployment = Comparing(df_Unemployment.Russia)
comparing_China_Unemployment = Comparing(df_Unemployment.China)
comparing_Afghanistan_Unemployment = Comparing(df_Unemployment.Afghanistan)
comparing_Japan_Unemployment = Comparing(df_Unemployment.Japan)
comparing_USA_Unemployment = Comparing(df_Unemployment["United States"])
plt.plot(comparing_Egypt_Unemployment.index,comparing_Egypt_Unemployment.values,'->',markerfacecolor = "yellow", label='Egypt')
for x, y in zip(comparing_Egypt_Unemployment.index, comparing_Egypt_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#065266', 'size':14})

plt.plot(comparing_Russia_Unemployment.index,comparing_Russia_Unemployment.values,'-*',markerfacecolor = "green" ,label='Russia')
for x, y in zip(comparing_Russia_Unemployment.index, comparing_Russia_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#596100', 'size':14})

plt.plot(comparing_China_Unemployment.index,comparing_China_Unemployment.values,'-o',markerfacecolor = "red",  label='China')
for x, y in zip(comparing_China_Unemployment.index, comparing_China_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#18540C', 'size':14})

plt.plot(comparing_Afghanistan_Unemployment.index,comparing_Afghanistan_Unemployment.values,'-^',markerfacecolor = "blue" , label='Afghanistan')
for x, y in zip(comparing_Afghanistan_Unemployment.index, comparing_Afghanistan_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#96005d', 'size':14})

plt.plot(comparing_USA_Unemployment.index,comparing_USA_Unemployment.values,'-x',markerfacecolor = "purple" , label='United States')
for x, y in zip(comparing_USA_Unemployment.index, comparing_USA_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#474747', 'size':14})

plt.plot(comparing_Japan_Unemployment.index,comparing_Japan_Unemployment.values,'-2',markerfacecolor = "gray",  label='Japan')
for x, y in zip(comparing_Japan_Unemployment.index, comparing_Japan_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#940025', 'size':14})

plt.title('Countries Unemployment rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#96005d')
plt.legend(fontsize=14)
plt.tight_layout()


# #### Understanding the Chart ..

# #### As we can see from chart that : 
#    ####    Afghanistan Unemployment rate Increased from 10.81 in 2000 to 11.16 in 2016.
#    ####    Russia Unemployment rate decreased from 10.58 in 2000 to 5.56 in 2016.
#    ####    Japan  Unemployment rate decreased from 4.75 in 2000 to 3.1 in 2016.
#    ####    Egypt Unemployment rate Increased from 8.95 in 2000 to 12.41 in 2016.
#    ####    USA Unemployment rate Increased from 3.99 in 2000 to 9.63 in 2010 surpassing Egypt by 0.68, and then decreased to  4.87 in 2016.
#    ####    China Unemployment rate Increased from 3.26 in 2000 to 4.53 in 2016.

#    ### ----------------------------------------------------------------------------------------------- #
# ### Egypt

# In[637]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_Egypt_Unemployment.index, comparing_Egypt_Unemployment.values,'->',markerfacecolor = "yellow", label='Egypt')
for x, y in zip(comparing_Egypt_Unemployment.index, comparing_Egypt_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#065266', 'size':14})

plt.title('Egypt Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper left")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'blue')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Egypt Unemployment rate Increased 3.46 in only 16 years ..

# #### Exploring more details ..

# In[649]:


df_Unemployment.Egypt.describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Russia

# In[639]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_Russia_Unemployment.index, comparing_Russia_Unemployment.values,'-*',color = "green",markerfacecolor = "yellow" ,label='Russia')
for x, y in zip(comparing_Russia_Unemployment.index, comparing_Russia_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#065266', 'size':14})

plt.title('Russia Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper right")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'green')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Russia Unemployment rate decreased 5.02 in only 16 years ..

# #### Exploring more details ..

# In[648]:


df_Unemployment["Russia"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### China

# In[640]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_China_Unemployment.index, comparing_China_Unemployment.values,'-o',color = "red",markerfacecolor = "yellow",  label='China')
for x, y in zip(comparing_China_Unemployment.index, comparing_China_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#18540C', 'size':14})

plt.title('China Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper left")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'red')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : China Unemployment rate Increased 1.27 in 16 years ..

# #### Exploring more details ..

# In[644]:


df_Unemployment["China"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Afghanistan

# In[641]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_Afghanistan_Unemployment.index, comparing_Afghanistan_Unemployment.values,'-^',color = "black",markerfacecolor = "red" , label='Afghanistan')
for x, y in zip(comparing_Afghanistan_Unemployment.index, comparing_Afghanistan_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#96005d', 'size':14})

plt.title('Afghanistan Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper left")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'black')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Afghanistan Unemployment rate Increased 0.35 in 16 years ..

# #### Exploring more details ..

# In[647]:


df_Unemployment["Afghanistan"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### United States

# In[642]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_USA_Unemployment.index, comparing_USA_Unemployment.values,'-x',color = "purple",markerfacecolor = "purple" , label='United States')
for x, y in zip(comparing_USA_Unemployment.index, comparing_USA_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#474747', 'size':14})
    
plt.title('United States Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper left")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = 'purple')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : USA Unemployment rate Increased 0.88 in 16 years ..

# #### Exploring more details ..

# In[646]:


df_Unemployment["United States"].describe()


#    ### ----------------------------------------------------------------------------------------------- #
# ### Japan

# In[643]:


plt.figure(figsize=(15,10),dpi= 65)
plt.plot(comparing_Japan_Unemployment.index, comparing_Japan_Unemployment.values,'-2',color = "#0e786c",markerfacecolor = "gray",  label='Japan')
for x, y in zip(comparing_Japan_Unemployment.index, comparing_Japan_Unemployment.values):
    t = plt.text(x, y,round(y, 2), verticalalignment='top' if y < 0 else 'bottom', 
                 fontdict={'color':'#940025', 'size':14})
plt.title('Japan Unemployment Rate..',fontsize=15)
plt.xlabel("Years")
plt.ylabel("Unemployment rate")
plt.legend(fontsize=14,loc= "upper left")
plt.grid(axis = 'x', linestyle='dashdot', alpha=1,color = '#0e786c')
plt.tight_layout()
plt.show()


# #### Understanding the Chart ..

# #### As we can see from chart that : Japan Unemployment rate Increased 1.65 in 16 years ..

# #### Exploring more details ..

# In[645]:


df_Unemployment["Japan"].describe()


# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='Question 5'></a>
# ### Question 5 : Which country has the most and least Unemployment Rate?

# ## Answer:

# #### Calulating the countries that has the most and least Unemployment rate ... 

# In[650]:


Unemployment = {}
for country in df_Unemployment.columns:
    Unemployment[df_Unemployment[country].mean()] = country


# ### Which country has the most Unemployment rate?

# In[651]:


print("The country with the most Unemployment rate is {} with an average of --> {} ....".format(Unemployment[max(Unemployment.keys())],max(Unemployment.keys())))


# ### Which country has the least Unemployment rate?

# In[653]:


print("The country with the least Unemployment Rate is {} with an average of --> {} ....".format(Unemployment[min(Unemployment.keys())],min(Unemployment.keys())))


#  ### ------------------------------------------------------------------------------------------------------------------------------------------------ ###
# 

# ## Dependant Questions..

# <a id='Question 6'></a>
# ### Question 6 : Does Unemployment rate have an effect on Murder rate ?

# #### Highest country in unemployment rate is North Macedonia ... Lets's investigate it ...

# ##### Macedonia Unemployment rate ..

# In[673]:


macdonia_Unemployment = df_Unemployment["North Macedonia"]


# In[674]:


macdonia_Unemployment.mean()


# ##### Macedonia Murder rate ..

# In[675]:


macdonia_Murder = murder_ratio["North Macedonia"]


# In[676]:


macdonia_Murder.mean()


# #### Lets visualize it and see ...

# In[691]:


plt.figure(figsize=(15,10), dpi= 65)
sns.histplot(macdonia_Murder.values, color="dodgerblue", label="Murder", kde=True,stat="density", linewidth=0.5)
sns.histplot(macdonia_Unemployment.values, color="orange", label="Unemployment", kde=True,stat="density", linewidth=0.5)
# Decoration
plt.title('North Macedonia', fontsize=15)
plt.ylabel("")
plt.legend()
plt.show()


# #### Answer :

# #### As we can see That the increase in Unemployent doesnt effect the Murder rate...

# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='Question 7'></a>
# ### Question 7 : Does increase in Income rate will lead to decrease the Murder rate ?

# #### Highest country in Income rate is Luxembourg ... Lets's investigate it ...

# ##### Luxembourg  Income rate ..

# In[693]:


income_Luxembourg = df_Income.Luxembourg


# In[705]:


income_Luxembourg.mean()


# ##### Luxembourg  Murder rate ..

# In[692]:


murder_Luxembourg = df_Murder.Luxembourg


# In[704]:


murder_Luxembourg.mean()


# #### Lets visualize it and see ...

# In[729]:


# Plot
fig, ax = plt.subplots(figsize=(15,10), dpi= 65)    
sns.stripplot(x=murder_Luxembourg, y= income_Luxembourg, jitter=0.25, size=8, ax=ax, linewidth=.5)
# Decorations
plt.title('Luxembourg', fontsize=14)
plt.ylabel("Income", fontsize=14)
plt.xlabel("Murder Rate", fontsize=14)
plt.grid(axis = 'y', linestyle='dashdot', alpha=0.2,color = '#0e786c')
plt.show()


# #### Answer :

# #### As we can see from the chart that decreasing the income rate increase the murder rate ,  like when the income was less than \\$70k the murder rate was 8.3 which is high rate .. But when the income increased to more than 100k the murder rate decreased by 2.74 ...

# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='Question 8'></a>
# ### Question 8 : Does the increase in Population effect the Unemployment Rate ?

# #### Highest country in Population is China  ... Lets's investigate it ...

# ##### China  Population ..

# In[752]:


Population_China = df_Population.China


# In[731]:


Population_China.mean()


# ##### China  Unemployment rate ..

# In[753]:


Unemployment_China = df_Unemployment.China


# In[733]:


Unemployment_China.mean()


# #### Lets visualize it and see ...

# In[762]:


plt.figure(figsize=(14,16), dpi= 65)
plt.scatter(Unemployment_China, Population_China, s=450, alpha=.6)
for x, y, tex in zip(Unemployment_China, Population_China, Unemployment_China):
    t = plt.text(x, y, round(tex, 1), horizontalalignment='center', 
                 verticalalignment='center', fontdict={'color':'white'})

# Decorations
# Lighten borders
plt.gca().spines["top"].set_alpha(.3)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(.3)
plt.gca().spines["left"].set_alpha(.3)

# plt.yticks(Unemployment_China.index)
plt.title('China', fontdict={'size':16})
plt.xlabel('Unemployment Rate',fontsize=16)
plt.ylabel("Population",fontsize=16)
plt.grid(linestyle='--', alpha=0.5)
# plt.xlim(-2.5, 2.5)
plt.show()


# #### Answer :

# #### As we can see from the chart that the increase in Population increases the Unemployment rate ..  Then the answer will be Yes the unemployment rate increases by increasing the population...

# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='Question 9'></a>
# ### Question 9: Does the increase in Murder rate effect the Economy?

# #### Highest country in Murder Rate is Brazil  ... Lets's investigate it ...

# ##### Brazil  Murder Rate ..

# In[763]:


Murder_Brazil = df_Murder.Brazil


# In[764]:


Murder_Brazil.mean()


# ##### Brazil GDP rate ..

# In[765]:


GDP_Brazil = df_GDP.Brazil


# In[766]:


GDP_Brazil.mean()


# #### Lets visualize it and see ...

# In[790]:


# Draw Plot
plt.figure(figsize=(15,10), dpi= 65)
plt.scatter(Murder_Brazil, GDP_Brazil, c=Murder_Brazil, cmap='plasma')
plt.colorbar()
plt.title('Brazil',fontsize=16)
plt.xlabel('Murder Rate',fontsize=16)
plt.ylabel('GDP Rate',fontsize=16)
plt.grid(alpha=0.5)
plt.show()


# #### Answer :

# #### As we can see from the chart that the increase in Murder rate doesnt Effect the Economy , As we can see that when Barzil had an 60000 murder rate its economy was increasing by a rate of 7.8 ..

# ## -------------------------------------------------------------------------------------------------------------------------- ###

# <a id='conclusions'></a>
# ## Conclusions
# 
# > We have investigated 5 indicators Unemplyment rate , Crime rate , GDP growth rate , Income Rate , Population rate .. 
# 
# > We compared countries and seen who has the most and least value of all the 5 indicators ...
# 
# > Which country has the most and least Murder rate?
# >> The country with the most Murder Rate is Brazil with an average of --> 52555.555555555555 ....
# 
# >> The country with the Least Murder Rate is Andorra with an average of --> 0.5137037037037038 ....
# 
# > Which is the most and least country in Population?
# >> The country with the most Population Rate is China with an average of --> 1308888888.8888888 ....
# 
# >> The country with the most Population Rate is Holy See with an average of --> 785.5925925925926 ....
# 
# > Which country has the most and least GDP Rate?
# >> The country with the most economy Growth is Equatorial Guinea with an average of --> 19.974110408814813 ....
# 
# >> The country with the least Growth is Ukraine with an average of --> -1.8408876753703698 ....
# 
# > Which country has the most and least Income Rate?
# >> The country with the most Income Rate is Luxembourg with an average of --> \\$95451.85185185185  ....
# 
# >>The country with the least Income Rate is Somalia with an average of --> \\$732.1481481481482 ....
# 
# > Which country has the most and least Unemployment Rate?
# >> The country with the most Unemployment rate is North Macedonia with an average of --> 30.729629517037043 ....
# 
# >> The country with the least Unemployment Rate is Kosovo with an average of --> 0.0 ....
# 
# > Does Unemployment rate have an effect on Murder rate ?
# >> No, the increase in Unemployent doesnt effect the Murder rate
# 
# > Does increase in Income rate will lead to decrease the Murder rate ?
# >> Yes, Increasing the income rate will decrease the murder rate ..
# 
# > Does the increase in Population effect the Unemployment Rate ?
# >> Yes, Increasing in Population will increase the Unemployment rate ..
# 
# > Does the increase in Murder rate effect the Economy?
# >> No, Increasing in Murder rate doesnt Effect the Economy ..
# 

# <a id='limitations'></a>
# ## Limitations
# 
# > There Was no nan limitaions since the years doesnt depend on each others .. So changing NaN Values to 0 didnt effect the analysis ..
# 
# > But there was a limations in years , Beaceause Not all data have the same amount years , Like the Unemployment data and GDP data both start from 1950 , but for Population data it starts from 1850 , same for Income Data it starts from 1800, But Murder Data starts from 1990 to 2016 , So i had to drop all the other years during visualization and keep years from 1990 to 2016 ,Inorder to be able to Visualize datas Evenly then compare them to each other... 
