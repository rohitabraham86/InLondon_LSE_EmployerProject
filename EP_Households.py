# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:53:30 2023

@author: adeli
"""

import pandas as pd
import numpy as np
import seaborn as sns

#define functions
def getnums(s, e,i):
   return list(range(s, e,i))

#identify file
file_households = 'C:/Users/adeli/OneDrive/Desktop/LSE DA/LSE_DA_Employer_Project_TW_London/households-borough.xlsx'
file_boroughs ='C:/Users/adeli/OneDrive/Desktop/LSE DA/LSE_DA_Employer_Project_TW_London/Borough Mapping.xlsx'

# # settlement_file = input('Enter the file name of the settlement file\n')
# settlement_file = 'C:/Users/adeli/OneDrive/Desktop/MamaC_files/MamaC_Automation/MamaC- Shopee Outbound Troubleshooting/99. Trash/december2022/Shopee Sales - December 2022.xls'
# settlement_object = pd.ExcelFile(settlement_file)                             # parse the xlsx file to get the meta data
# tabs = settlement_object.sheet_names                                          # get the tab names of the xlsx file
# wanted_tabs = [i for i in tabs if 'income' in i]                              # identify the wanted tabs be searching for 'income'
# all_dfs = pd.read_excel(settlement_file, skiprows=[0,1,2,3,4], sheet_name=wanted_tabs) # read in all data from wanted tabs whilst excluding unwanted top rows
# settlement_df = pd.concat(all_dfs, ignore_index=True)                         # concatenate the data into a single dataframe
# settlement = list(settlement_df['No. Pesanan'])                               # extract the 'No. Pesanan' column and store as a list


#read vehicles file and convert to single dataframe with column informing the excel tab name for each row
workbook_households = pd.ExcelFile(file_households)
sheets_households = getnums(2010,2021,1)
sheets_households = [str(x) for x in sheets_households] #convert sheet_vehicles from int to str
data_households = pd.read_excel(workbook_households, skiprows =[0] , usecols = [0,1,2,3,4,5,6], sheet_name = sheets_households)

households = pd.DataFrame()
for name, frame in data_households.items():
    frame['Year'] = name
    households = households.append(frame)

#read borough file
borough = pd.read_excel(file_boroughs)

#data cleaning 
#households = households.rename(columns={'Unnamed: 0':'Area Code','Unnamed: 1':'Local Authority'}, inplace = True)
households.replace({'-', None})
households = households.dropna(subset = ['Total']) #remove rows with missing location details
households = households.dropna(subset = ['Unnamed: 0']) #remove rows with missing location details
households = households.dropna(subset = ['Unnamed: 1']) #remove rows with missing location details

#merge with borough information
households_boroughs = households.merge(borough, left_on = 'Unnamed: 1', right_on = 'Borough Name', how = 'inner')

# #create visualisation
# vehicles_barplot = sns.barplot(vehicles_boroughs, x = 'Year', y = 'Cars', hue = 'Borough Name')