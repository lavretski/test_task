"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""

# TODO Import the necessary libraries
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# TODO Import the dataset
#done in others

path = r'./data/weather_dataset.data'

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
dateparse = lambda y,m,d: pd.to_datetime('19{}-{}-{}'.format(y,m,d))
columns = pd.read_csv(path, nrows=1).columns
def converter(value:str):
    try:
         float(value)
         return value
    except:
        return "NaN"
converterS = {col: converter for col in list(columns)[0].split()[3:]}
data = pd.read_csv(path, skiprows=1, sep="\s+", parse_dates=[[0,1,2]], date_parser=dateparse, converters=converterS)

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
data = pd.concat((data.loc[:,  "Yr_Mo_Dy"], data.loc[:, "loc1" : ].astype('float')), axis=1)
data_fixed = data.dropna()
data_fixed[data_fixed > 3 * data_fixed.std() + data_fixed.mean()] = np.nan
#I don't remove very small values, but since you inserted them manually there should be few
data_fixed.dropna(inplace=True)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it
#done in others

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data_fixed.set_index('Yr_Mo_Dy', inplace=True)

# TODO Compute how many values are missing for each location over the entire record
print(data.isna().sum(axis=1))


# TODO Compute how many non-missing values there are in total
print("non-missing values there are in total", (data.isna() == False).sum().sum())


# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
#print("the mean windspeeds of the windspeeds over all the locations and all the times with a very windy day", np.nanmean(data_fixed.loc[:, 'loc1':]))
#It was a very windy day
#print("monster", any(data_fixed.loc[:, 'loc1':] > 100000000000))
#data_fixed[data_fixed > 3 * data_fixed.std() + data_fixed.mean()] = np.nan
#data_fixed.dropna(inplace=True)
print("the mean windspeeds of the windspeeds over all the locations and all the times without a very windy day",
      np.nanmean(data_fixed))

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = pd.DataFrame()
loc_stats['min'] = data_fixed.min()
loc_stats['max'] = data_fixed.max()
loc_stats['mean'] = data_fixed.mean()
loc_stats['std'] = data_fixed.std()
print(loc_stats)

# TODO Find the average windspeed in January for each location
print("average windspeed in January for each location", data_fixed[data_fixed.index.to_series().dt.month==1].mean())

# TODO Downsample the record to a yearly frequency for each location
print(data_fixed.resample('AS-JAN').mean())

# TODO Downsample the record to a monthly frequency for each location
print(data_fixed.resample('M').mean())

# TODO Downsample the record to a weekly frequency for each location
print(data_fixed.resample('W-MON').mean())

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
w = data_fixed.resample('W').agg(['min','max','mean','std'])
print(w.loc[w.index[:23], :])