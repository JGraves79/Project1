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

ndf=ndf.groupby('District').sum()


ndf=ndf.groupby('District').sum()
ndf3=ndf.iloc[:10,:]
ndf3[['Electric Vehicle Type_Plug-in Hybrid Electric Vehicle (PHEV)','Electric Vehicle Type_Battery Electric Vehicle (BEV)']].plot(kind='bar', legend=True)
plt.title('BEV vs. PHEV')
plt.xlabel('District')
plt.ylabel('Number of Vehicles')
plt.legend(title='Vehicle Type')
plt.show()
