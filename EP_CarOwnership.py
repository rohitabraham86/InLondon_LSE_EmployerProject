# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:44:40 2023

@author: adeli
"""

import pandas as pd
import numpy as np
import seaborn as sns

#define functions
def getnums(s, e,i):
   return list(range(s, e,i))

#identify file
file_vehicles = 'C:/Users/adeli/OneDrive/Desktop/LSE DA/LSE_DA_Employer_Project_TW_London/vehicles-licensed-type-borough.xls'
sheets_vehicles = getnums(2010,2022,1)
sheets_vehicles = [str(x) for x in sheets_vehicles] #convert sheet_vehicles from int to str
file_boroughs ='C:/Users/adeli/OneDrive/Desktop/LSE DA/LSE_DA_Employer_Project_TW_London/Borough Mapping.xlsx'

#read vehicles file and convert to single dataframe with column informing the excel tab name for each row
workbook_vehicles = pd.ExcelFile(file_vehicles)
data_vehicles = pd.read_excel(workbook_vehicles, sheet_name= sheets_vehicles)
vehicles = pd.DataFrame()
for name, frame in data_vehicles.items():
    frame['Year'] = name
    vehicles = vehicles.append(frame)

#read borough file
borough = pd.read_excel(file_boroughs)

#data cleaning 
vehicles = vehicles.dropna(subset = ['ONS CHD LA Code']) #remove rows with missing location details
vehicles = vehicles.dropna(subset = ['ONS SNAC LA Code']) #remove rows with missing location details
#vehicles = vehicles.rename(columns = {'Local Authority  ':'Authority'}, inplace = True)
vehicles['Cars'] = vehicles['Cars'].astype(int)
vehicles['Motor cycles'] = vehicles['Motor cycles'].astype(int)
vehicles['Light goods'] = vehicles['Light goods'].astype(int)
vehicles['Heavy goods'] = vehicles['Heavy goods'].astype(int)
vehicles['Buses and coaches'] = vehicles['Buses and coaches'].astype(int)
vehicles['Other vehicles'] = vehicles['Other vehicles'].astype(int)
vehicles['Total'] = vehicles['Total'].astype(int)
vehicles['Year'] = vehicles['Year'].astype(int)

#merge with borough information
vehicles_boroughs = vehicles.merge(borough, left_on = 'Local Authority  ', right_on = 'Borough Name', how = 'outer')

#create visualisation
vehicles_barplot = sns.barplot(vehicles_boroughs, x = 'Year', y = 'Cars', hue = 'Borough Name')



#concatdata_vehicles.to_excel('C:/Users/adeli/OneDrive/Desktop/LSE DA/LSE_DA_Employer_Project_TW_London/data_vehicles.xlsx')
