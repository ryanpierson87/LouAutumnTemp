#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:46:35 2018

@author: ryanpierson
"""

import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
#import numpy as np


def create_database(connection):
    
    df = pd.read_csv('1502536.csv', low_memory=False)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['YEAR'], df['MONTH'], df['DAY'] = df['DATE'].dt.year, df['DATE'].dt.month, df['DATE'].dt.day
    
    #locations table
    df_loc = df[['STATION', 'NAME','LATITUDE', 'LONGITUDE', 'ELEVATION']].copy()
    df_loc.drop_duplicates(inplace=True)
    df_loc = df_loc[['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION']].set_index('STATION')
    df_loc.to_sql('locations', connection, if_exists='replace')
    
    #weather table
    df_weather = df[['STATION', 'DATE', 'YEAR', 'MONTH', 'DAY','TMAX','TMIN']].copy()
    df_weather.to_sql('weather', connection, if_exists='replace')

   



############ Configure the data
def main():
    conn = sqlite3.connect('weather.db')
    
    
    create_database(conn)
    
    x= "grey"
    
    #### Generate the graphs from the database
    weather = pd.read_sql('select DATE, (TMAX+TMIN)/2 Temp, TMAX high, TMIN low, YEAR, MONTH, DAY from weather where station = "USW00093821" and YEAR < 2018', conn)
    
    #Plot Years
    plt.subplots(figsize=(20,10))
    sns.boxplot(x=weather['YEAR'], y=weather['Temp'], color="#6699ff").set_title("Box Yearly Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    plt.subplots(figsize=(20,10))
    sns.violinplot(x=weather['YEAR'], y=weather['Temp'], color="#6699ff").set_title("Violin Yearly Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    
    #Box/Violin plots of Autumn
    autumn = weather[weather['MONTH'].isin([9, 10, 11])]
    plt.subplots(figsize=(20,10))
    sns.boxplot(x=autumn['YEAR'], y=autumn['Temp'], color="#ff7733").set_title("Box Autumnal Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    plt.subplots(figsize=(20,10))
    sns.violinplot(x=autumn['YEAR'], y=autumn['Temp'], color="#ff7733").set_title("Violin Autumnal Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    
    
if __name__ == '__main__':
    main()