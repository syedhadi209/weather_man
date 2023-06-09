import sys
import os
import csv
from operator import itemgetter
import numpy as np
import colorama
from colorama import Fore

user_input = sys.argv[1]

path = "/home/dev/Desktop/pp-1/lahore_weather"



def assignData(row,max_temp,min_temp,max_humid):
    if len(row) > 1 and row[0] != 'PKT':
        if row[1] != '' and row[3] != '' and row[7]!='':
            if int(row[1]) >= max_temp[1] and row[1] != '':
                max_temp[0] = row[0]
                max_temp[1] = int(row[1])

            if min_temp[1] == 0:
                min_temp[1] = int(row[3])

            if int(row[3]) <= min_temp[1]:
                min_temp[1] = int(row[3])
                min_temp[0] = row[0]

            if int(row[7]) >= max_humid[1]:
                max_humid[0] = row[0]
                max_humid[1] = int(row[7])


def readData(specific_year,i, max_temp,min_temp,max_humid, max_, min_,humid_):
    with open(f"{path}/{specific_year[i]}", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            assignData(row,max_temp,min_temp,max_humid)

        mon = specific_year[i].split("_")[-1].split(".")[0]                
        max_temp.append(mon)
        min_temp.append(mon)
        max_humid.append(mon)


        max_.append(max_temp)
        min_.append(min_temp)
        humid_.append(max_humid)


def getData(specific_year, max_, min_,humid_):
    for i in range(len(specific_year)):
        max_temp = ['',0]
        min_temp = ['',0]
        max_humid = ['',0]

        readData(specific_year,i,max_temp,min_temp,max_humid,max_,min_,humid_)


def printYearData(year, highest, lowest, humid):
    print(f"Data for year : {year}")
    print(f"Highest: {highest[1]}C on {highest[-1]} {highest[0].split('-')[-1]}")
    print(f"Lowest: {lowest[1]}C on {lowest[-1]} {lowest[0].split('-')[-1]}")
    print(f"Humid: {humid[1]}% on {humid[-1]} {humid[0].split('-')[-1]}")
    


def check_for_year(year):
    files = os.listdir(path)
    specific_year = [file for file in files if year in file]

    max_ = []
    min_ = []
    humid_ = []

    getData(specific_year,max_,min_,humid_)

    if len(max_) != 0:
        highest = sorted(max_,key = itemgetter(1))[-1]
        lowest = sorted(min_,key = itemgetter(1))[0]
        humid = sorted(humid_,key=itemgetter(1))[-1]

        printYearData(year,highest,lowest,humid)

    else:
        print("Data for this year is not avaiable!!!!!!!!")

def calculate_Temperature_Humidity(specific_year,avg_temp,avg_humidity,month):
    flag = False
    for mon in specific_year:
        if mon.split("_")[-1].split(".")[0] == month[0:3]:
            print("Data for "+mon.split("_")[-1].split(".")[0])
            flag = True
            with open(f"{path}/{mon}", 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if len(row) > 1 and row[0] != 'PKT':
                        avg_temp.append(int(row[2]))
                        avg_humidity.append(int(row[8]))

    return flag


def printMonthData(avg_temp,avg_humidity):
    print(f"Highest Average: {max(avg_temp)}C")
    print(f"Lowest Average: {min(avg_temp)}C")
    print(f"Average Humidity: {int(np.mean(avg_humidity))}%")


def check_for_month(year,month):
    files = os.listdir(path)
    specific_year = [file for file in files if year in file]
    flag = False

    avg_temp = []
    avg_humidity = []

    flag = calculate_Temperature_Humidity(specific_year,avg_temp,avg_humidity,month)
    

    if flag:
        printMonthData(avg_temp,avg_humidity)
        
    else:
        print("Invalid Month entered")


def draw_bar(year,month):
    files = os.listdir(path)
    specific_year = [file for file in files if year in file]
    flag = False

    for mon in specific_year:
        if mon.split("_")[-1].split(".")[0] == month[0:3]:
            print("Data for "+mon.split("_")[-1].split(".")[0])
            flag = True
            with open(f"{path}/{mon}", 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if len(row) > 1 and row[0] != 'PKT':
                        draw(row[0],int(row[1]),1)
                        draw(row[0],int(row[3]),0)


def draw(date,count,color):
    var = date.split('-')[-1]
    print(Fore.WHITE, var + " ",end='')
    for i in range(count):
        if color:
            print(Fore.RED + '+',end='')
        else:
            print(Fore.BLUE + '+',end='')
    
    print(Fore.WHITE,count)
    print('\n')




# def switch(argument):
#     if argument == "-e":
#         try:
#             year = sys.argv[2]
#             if len(year) == 4:
#                 check_for_year(year)
#             else:
#                 print("Invalid Input")
#         except:
#             print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")

#     elif argument == "-a":
#         try:
#             year = sys.argv[2]
#             if len(year) == 4:
#                 month = sys.argv[3].capitalize()
#                 check_for_month(year=year,month=month)
#             else:
#                 print("Input correct format of year")
#         except:
#             print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")


#     elif argument == "-c":
#         try:
#             year = sys.argv[2]
#             if len(year) == 4:
#                 month = sys.argv[3].capitalize()
#                 draw_bar(year=year,month=month)
#             else:
#                 print("Input correct format of year")
#         except:
#             print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")

#     else:
#         print("Invalid Input")


if user_input == "-e":
    try:
        year = sys.argv[2]
        if len(year) == 4:
            check_for_year(year)
        else:
            print("Invalid Input")
    except:
        print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")



elif user_input == "-a":
    
    try:
        year = sys.argv[2]
        if len(year) == 4:
            month = sys.argv[3].capitalize()
            check_for_month(year=year,month=month)
        else:
            print("Input correct format of year")
    except:
        print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")


elif user_input == "-c":
    
    try:
        year = sys.argv[2]
        if len(year) == 4:
            month = sys.argv[3].capitalize()
            draw_bar(year=year,month=month)
        else:
            print("Input correct format of year")
    except:
        print("Insert correct parametrs [weather_man.py -a year(yyyy) month(Mar)]")

    


