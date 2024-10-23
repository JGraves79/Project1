#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:53:06 2024

@author: Shanice931
"""

import pandas as pd

import matplotlib.pyplot as plt


# Load the CSV into a DateFrame
df = pd.read_csv('/Users/Shanice931/data analysis/Project1/EV Data cleaned.csv')


# Create New DataFrame with variables
df2=df[['District','Electric Vehicle Type']]
ndf=pd.get_dummies(df2,columns=['Electric Vehicle Type'])
ndf.keys()
ndf['Electric Vehicle Type_Battery Electric Vehicle (BEV)']=ndf['Electric Vehicle Type_Battery Electric Vehicle (BEV)'].astype(int)
ndf['Electric Vehicle Type_Plug-in Hybrid Electric Vehicle (PHEV)']=ndf['Electric Vehicle Type_Plug-in Hybrid Electric Vehicle (PHEV)'].astype(int)

# Plot the data 
ndf.plot(kind='bar', x='District', y='[Electric Vehicle Type_Plug-in Hybrid Electric Vehicle (PHEV)]''[Electric Vehicle Type_Battery Electric Vehicle (BEV)]', legend=False)
plt.title('Electric Vehicle Type_Battery Electric Vehicle (BEV) vs. Electric Vehicle Type_Plug-in Hybrid Electric Vehicle (PHEV)')
plt.xlabel('District')
plt.ylabel('Number of Vehicle')
plt.legend(title='District')
plt.show()

# Plot the data 
D_index = ndf['District'].value_counts()
plt.figure(figsize=(20, 10))  
D_index.plot(kind='bar', rot=70)
plt.xlabel('District')
plt.ylabel('EV Type')
