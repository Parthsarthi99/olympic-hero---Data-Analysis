# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts




data['Better_Event'] = np.where((data['Total_Summer']>data['Total_Winter']),'Summer', 'Winter')
data['Better_Event']= np.where((data['Total_Summer']==data['Total_Winter']),'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
top_countries = top_countries[:-1]
def top_ten(df, cname):
    country_list = list((df.nlargest(10, cname)['Country_Name']))
    return country_list
top_10_summer = top_ten(top_countries, 'Total_Summer')
print(top_10_summer)
top_10_winter = top_ten(top_countries, 'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
print(top_10)
common = [v for v in top_10_summer if v in top_10_winter and top_10]
print(common)





# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
plt.figure(figsize=(15,5))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.title('Top 10 Summer')
plt.xlabel('Country Name')
plt.ylabel('Total Medal')

winter_df = data[data['Country_Name'].isin(top_10_winter)]
plt.figure(figsize=(15,5))
plt.bar(summer_df['Country_Name'], summer_df['Total_Winter'])
plt.title('Top 10 Winter')
plt.xlabel('Country Name')
plt.ylabel('Total Medal')

top_df = data[data['Country_Name'].isin(top_10)]
plt.figure(figsize=(15,5))
plt.bar(summer_df['Country_Name'], summer_df['Total_Medals'])
plt.title('Top 10')
plt.xlabel('Country Name')
plt.ylabel('Total Medal')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print("Summer Gold winner is ",summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total'])
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('Best country is ', best_country)


# --------------
#Code starts here

#bestcountry all details
best = data[data['Country_Name'] == best_country]

#Subsetting best 
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

#Creating a bar plot
best.plot.bar(stacked = True)

#Labelling X co-ordinate
plt.xlabel('United States')

#Labelling Y co-ordinate
plt.ylabel('Medals Tally')

#Rotating the X-labels
plt.xticks(rotation=45)



