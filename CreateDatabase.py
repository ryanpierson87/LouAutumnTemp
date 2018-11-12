#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:05:51 2018

@author: ryanpierson
"""

import pandas as pd
import sqlite3

def main():
    conn = sqlite3.connect('weather.db')
    df = pd.read_csv('/Users/ryanpierson/Downloads/1502536.csv', low_memory=False)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['YEAR'], df['MONTH'], df['DAY'] = df['DATE'].dt.year, df['DATE'].dt.month, df['DATE'].dt.day
    #locations table
    df_loc = df[['STATION', 'NAME','LATITUDE', 'LONGITUDE', 'ELEVATION']].copy()
    df_loc.drop_duplicates(inplace=True)
    df_loc = df_loc[['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION']].set_index('STATION')
    df_loc.to_sql('locations', conn)
    #weather table
    df_weather = df[['STATION', 'DATE', 'YEAR', 'MONTH', 'DAY','TMAX','TMIN']].copy()
    df_weather.to_sql('weather', conn)
    
if __name__ == '__main__':
    main()