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
    
    x= "grey"
    
    conn = sqlite3.connect('weather.db')
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
    sns.boxplot(x=autumn['YEAR'], y=autumn['Temp'], color="#e64d00").set_title("Box Autumnal Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    plt.subplots(figsize=(20,10))
    sns.violinplot(x=autumn['YEAR'], y=autumn['Temp'], color="#e64d00").set_title("Violin Autumnal Comparison of Temperatures")
    plt.grid(axis='y', color=x)
    
    
if __name__ == '__main__':
    main()