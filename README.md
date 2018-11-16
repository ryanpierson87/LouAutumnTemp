Code Louisville Project analyzing Autumal weather data for Louisville to figure out what Louisville Temperatures have looked like since 2002 and to answer the question of
"Is Louisville losing it's Autumnal Season"? (It doesn't appear so).

This project uses data retrieved from the NOAA as a CSV file, loading it into a pandas dataframe and then input that data into a sql database.

This project, from the Jupyter Notebook, uses a few different ways of analyzing the data: 
1. a graph to plot the number of hottest days per year(2012 appears to have the largest quantity of hot days for the provided timeframe)
2. a graph of each month to plot the progression of temperatures for each years
3. Box/Violin plots to evaluate the temperatures for each year(sans 2018)
4. Box/Violin plot to evaluate the autumns(September, October, November) for each year(sans 2018)

The project aims to investigate autumnal temperatures from 2002-2017 and to give a yearly context of the progression of temperatures.

IPython Notebook requires: pandas, sqlite3, matplotlib, bokeh, and seaborn modules.
Python file requires: pandas, sqlite3, matplotlib, and seaborn modules.

(Note: for some reason, the Jupyter Notebook cell needs to be ran a second time to display the seaborn plots.
    The bokeh visuals are not included in the .py file)