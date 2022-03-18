# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:02:08 2022

@author: Shreyas Datar, Student ID: 21031242
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#FUNCTION DEFINITIONS

#Pie chart
def plot_pie(seats, no_seats, title_p):
    plt.pie((no_seats/seats.count())*100, labels=no_seats.index, autopct='%.1f%%')
    plt.title(title_p)



#Violin Plot
def plot_violin(data, title_v, lab_x):
    plt.violinplot(file_csv["AccelSec"], showmeans=True)
    plt.title(title_v)
    plt.xlabel(lab_x)

#Bar Graph (Single Value, Multivalue)
def plot_bar(x, y):
    plt.bar(x, y, align='center')


#VISUALISING DATA FROM CSV FILE USING ABOVE FUNCTIONS

#Reading CSV file data into variable
file_csv = pd.read_csv("ElectricCarData_Clean.csv")



#Variables and function call for pie chart
seats = file_csv["Seats"]
no_seats = file_csv["Seats"].value_counts()
title = "Percentage of number of seats"
plot_pie(seats, no_seats, title)

#Variables and function call for violinplot
plt.subplot(1,5,1)
#plot1 Acceleration
plot_violin(file_csv["AccelSec"], "Acceleration", "EVs")

plt.subplot(1,5,3)
#plot2 Efficiency
plot_violin(file_csv["Efficiency_WhKm"], "Effeciency", "EVs")

plt.subplot(1,5,5)
#plot3 Price
plot_violin(file_csv["PriceEuro"], "Price", "EVs")

#Variables and function call for single value Bar Graph
brand = file_csv["Brand"].value_counts()
plt.figure()
plot_bar(brand.index, brand.values)
plt.xlabel("Brands")
plt.ylabel("No. of EVs")
plt.xticks(size=8, rotation=-90)
plt.yticks(range(15))
plt.show()

#Variables and function call for multivalue Bar Graph
Bar = file_csv.groupby(["Brand", "BodyStyle"]).sum() #using groupby to get desired data
#print(Bar.index)
Bar = Bar.reset_index() # to convert indexed columns back to regular columns 
                        # (try Bar.index to understand)
                        
audi = Bar[Bar["Brand"] == "Audi "][["BodyStyle", "one"]]
tesla = Bar[Bar["Brand"] == "Tesla "][["BodyStyle", "one"]]
nissan = Bar[Bar["Brand"] == "Nissan "][["BodyStyle", "one"]]
plt.figure()
plot_bar(tesla["BodyStyle"], tesla["one"].to_numpy())
plot_bar(audi["BodyStyle"], audi["one"].to_numpy())
plot_bar(nissan["BodyStyle"], nissan["one"].to_numpy())
plt.legend(["Tesla", "Audi", "Nissan"])
plt.show()
