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


    



############ Configure the data
def main():
    #output_notebook()
    conn = sqlite3.connect('weather.db')
    weather = pd.read_sql('select DATE, (TMAX+TMIN)/2 Temp, TMAX high, TMIN low, YEAR, MONTH, DAY from weather where station = "USW00093821"', conn)
    plt.subplots(figsize=(20,10))
    sns.boxplot(x=weather['YEAR'], y=weather['high'])
    plt.grid(axis='y', color='lightblue')
    plt.subplots(figsize=(20,10))
    sns.violinplot(x=weather['YEAR'], y=weather['high'])
    plt.grid(axis='y', color='lightblue')
    

if __name__ == '__main__':
    main()