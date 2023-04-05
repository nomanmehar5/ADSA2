# -*- coding: utf-8 -*-
"""
importing libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def wbdata(filename,filename1,width,filename2,filename3):
    """
        this function reads the Data of Total Populaion from World Bank Data
        manipulate it, using describe funcion to show statistics properties,
        Calculate Mean, Median and Standard Deviation and ploting the 
        graphs 
        
    """
    
    #Read the data
    df = pd.read_csv(filename, skiprows = 4)
       
    #Drop the columns we don't need from the data 
    df = df.drop(columns=["Country Code" ,
                          'Indicator Name' , 
                          'Indicator Code'])
    
    #Setting the country name as a Index
    df = df.set_index('Country Name')
            
    #Get the only countries we need data from        
    df = df.loc[['India', 'Pakistan', 'Afghanistan']]
    
    #Select the data for last 10 years 
    df1 = df.iloc[:,20::5]
    
    #Describe funcion give me the statistics of all coulumns
    des = df1.describe()
    
    print(des)
        
    #Transpose data
    df1 = df1.T
    
    print(df1)
                       
    """
    Plot - 1 = Total Population
    """
    #Individual columns for data 
    country_1 = df1["India"]
    country_2 = df1["Pakistan"]
    country_3 = df1["Afghanistan"]
    
    #X-axis of our line plot
    years = df1.index
    
    #figure size
    plt.figure(figsize=(12, 6))
            
    #plot the line chart of Total Populaion of three countries
    plt.plot(years, country_1, label='India')
    plt.plot(years, country_2, label='Pakistan')
    plt.plot(years, country_3, label='Afghanistan')
    
    #Title of the line chart
    plt.title("Total Populaion of India, Pakistan and Afghanistan")

    #Title of the X label
    plt.xlabel("years")

    #Title of the Y label
    plt.ylabel("Values")

    #Show Legends to identify which colour belongs to which country
    plt.legend()
           
    plt.show()
    
    """
    Calculate the mean, Median and Standard Deviation of India, Pakistan
    and Afghanistan
    """
    mean_of_Ind = np.mean(df1['India'])
    median_of_Ind = np.median(df1['India'])
    Standard_Deviation_of_Ind = np.std(df1['India'])
    
    print("\nMean of India is = ", mean_of_Ind)
    print("Median of India is = ", median_of_Ind)
    print("Standard Deviation of India is = ", Standard_Deviation_of_Ind)
    
    mean_of_Pak = np.mean(df1['Pakistan']).mean()
    median_of_Pak = np.median(df1['Pakistan'])
    Standard_Deviation_of_Pak = np.std(df1['Pakistan'])
    
    print("\n\nMean of Pakistan is = ", mean_of_Pak)
    print("Median of Pakistan is = ", median_of_Pak)
    print("Standard Deviation of Pakistan is = ", Standard_Deviation_of_Pak)
    
    mean_of_Afg = np.mean(df1['Afghanistan']).mean()
    median_of_Afg = np.median(df1['Afghanistan'])
    Standard_Deviation_of_Afg = np.std(df1['Afghanistan'])
    
    print("\n\nMean of Afghanistan is = ", mean_of_Afg)
    print("Median of Afghanistan is = ", median_of_Afg)
    print("Standard Deviation of Afghanistan is = ", Standard_Deviation_of_Afg)
    
    values_mean = [mean_of_Ind, mean_of_Pak, mean_of_Afg]
    values_median = [median_of_Ind, median_of_Pak, median_of_Afg]
    values_sd = [Standard_Deviation_of_Ind, 
                 Standard_Deviation_of_Pak, 
                 Standard_Deviation_of_Afg]
    countries_sta = ['India', 'Pakistan', 'Afghanistan']
    
    X_axis_sta = np.arange(len(countries_sta))
    
    #figure size
    #plt.figure(figsize=(10, 6))
    
    # Create the bar plot
    plt.bar(X_axis_sta, values_mean, width, label='Mean')
    plt.bar(X_axis_sta + width, values_median, width, label='Median')
    plt.bar(X_axis_sta + width*2, values_sd, width, label='Standard_Deviation')

    #Title of the line chart
    plt.title("Bar plot with the values of countries")

    #Title of the X label
    plt.xlabel("Countries")

    #Title of the Y label
    plt.ylabel("Values")

    plt.xticks(X_axis_sta + width, countries_sta)

    #Show Legends to identify which colour belongs to which year
    plt.legend()

    plt.show()
    
    """
        plot 2 = Agriculture land
        in this data set we plot the agriculture land of Pakistan, India
        and Afghanistan with the duration of every 5 years
    """
    #Read the dataset
    Agri_land = pd.read_csv(filename1, skiprows = 4)
    
    #Drop the columns we don't need from the data 
    Agri_land = Agri_land.drop(columns=["Country Code" ,
                          'Indicator Name' , 
                          'Indicator Code'])
    
    #Setting the country name as a Index
    Agri_land = Agri_land.set_index('Country Name')
            
    #Get the only countries we need data from        
    Agri_land = Agri_land.loc[['India', 'Pakistan', 'Afghanistan']]
    
    #Select the data 
    Agri_land = Agri_land.iloc[:,20::5]
    
    #Transpose data
    df_Agri_land = Agri_land.T
    
    #print(df_ARB_land)    
          
    #Individual columns for data 
    country_1 = df_Agri_land["India"]
    country_2 = df_Agri_land["Pakistan"]
    country_3 = df_Agri_land["Afghanistan"]
    
    #X-axis of our line plot
    years = df_Agri_land.index
    
    #figure size
    plt.figure(figsize=(8, 6))
            
    #plot the line chart of Total Populaion of three countries
    plt.plot(years, country_1, label='India')
    plt.plot(years, country_2, label='Pakistan')
    plt.plot(years, country_3, label='Afghanistan')
    
    #Title of the line chart
    plt.title("Agriculture Land of India, Pakistan and Afghanistan")

    #Title of the X label
    plt.xlabel("years")

    #Title of the Y label
    plt.ylabel("Values")

    #Show Legends to identify which colour belongs to which country
    plt.legend()
           
    #Show Plot
    plt.show()

    
    
    """
        plot 3 = Arable land
        in this dataset, we compare the Arable Land of Pakistan, India
        and Afghanistan with the duration of every 5 years
    """
    #Read the data
    ARB_land = pd.read_csv(filename3, skiprows = 4)
       
    #Drop the columns we don't need from the data 
    ARB_land = ARB_land.drop(columns=["Country Code" ,
                          'Indicator Name' , 
                          'Indicator Code'])
    
    #Setting the country name as a Index
    ARB_land = ARB_land.set_index('Country Name')
            
    #Get the only countries we need data from        
    ARB_land = ARB_land.loc[['India', 'Pakistan', 'Afghanistan']]
    
    #Select the data 
    ARB_land = ARB_land.iloc[:,20::5]
    
    #Transpose data
    df_ARB_land = ARB_land.T
    
    #print(df_ARB_land)    
          
    #Individual columns for data 
    country_1 = df_ARB_land["India"]
    country_2 = df_ARB_land["Pakistan"]
    country_3 = df_ARB_land["Afghanistan"]
    
    #X-axis of our line plot
    years = df_ARB_land.index
    
    #figure size
    plt.figure(figsize=(8, 6))
            
    #plot the line chart 
    plt.plot(years, country_1, label='India')
    plt.plot(years, country_2, label='Pakistan')
    plt.plot(years, country_3, label='Afghanistan')
    
    #Title of the line chart
    plt.title("Arable Land of India, Pakistan and Afghanistan")

    #Title of the X label
    plt.xlabel("years")

    #Title of the Y label
    plt.ylabel("Values")

    #Show Legends to identify which colour belongs to which country
    plt.legend()
           
    plt.show()
    
    """
        plot 4 = Forest land
        in this dataset, we compare the Forest Land of Pakistan, India
        and Afghanistan with the duration of every 5 years
    """
    #Read the data
    FT_land = pd.read_csv(filename2, skiprows = 4)
       
    #Drop the columns we don't need from the data 
    FT_land = FT_land.drop(columns=["Country Code" ,
                          'Indicator Name' , 
                          'Indicator Code'])
    
    #Setting the country name as a Index
    FT_land = FT_land.set_index('Country Name')
            
    #Get the only countries we need data from        
    FT_land = FT_land.loc[['India', 'Pakistan', 'Afghanistan']]
    
    #Select the data 
    FT_land = FT_land.iloc[:,20::5]
    
    #Transpose data
    df_FT_land = FT_land.T       
         
    #Individual columns for data 
    country_1 = df_FT_land["India"]
    country_2 = df_FT_land["Pakistan"]
    country_3 = df_FT_land["Afghanistan"]
    
    #X-axis of our line plot
    years = df_FT_land.index
    
    #figure size
    plt.figure(figsize=(8, 6))
            
    #plot the line chart of Total Populaion of three countries
    plt.plot(years, country_1, label='India')
    plt.plot(years, country_2, label='Pakistan')
    plt.plot(years, country_3, label='Afghanistan')
    
    #Title of the line chart
    plt.title("Forest Land of India, Pakistan and Afghanistan")

    #Title of the X label
    plt.xlabel("years")

    #Title of the Y label
    plt.ylabel("Values")

    #Show Legends to identify which colour belongs to which country
    plt.legend()
           
    plt.show()
    
    """
        plot 6 = Changes in Forest land
        in this dataset, we show the changes of Forest Land of Pakistan 
        in every 5 years
    """
    
    plt.plot(years, country_2, label='Pakistan')
    
    #Title of the line chart
    plt.title("Changes in Forest Land of Pakistan")

    #Title of the X label
    plt.xlabel("years")

    #Title of the Y label
    plt.ylabel("Values")

    #Show Legends to identify which colour belongs to which country
    plt.legend()
           
    plt.show()
        
link1 = 'Total_pop.csv'
link2 = 'Agriculturalland.csv'
link3 = 'Forestarea.csv'
link4 = 'Arableland.csv'

wbdata(link1,link2,0.1,link3,link4)
