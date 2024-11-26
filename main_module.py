# import functions and library
import time as t
import csv
import matplotlib.pyplot as plt
import numpy as np


def showMenu():  # Menu function
    print('=' * 100)
    print('''Please make a selection
        Option A: Display the number of vehicles crossed at the different cities in 2011
        Option B: Display The mean and values that exceed the mean
        Option C: Display vehicle data which has decreased by at least 5% from the previous year
        Option D: Display plot
        Option Q:Exit the program''')
    print('=' * 100)


def loadCSVData(fname):  # CSV Reader
    datalist = []  # Creates empty datalist
    openfile = open(fname)  # open's csv file
    csvreader = csv.reader(openfile)  # assigns csvreader variable to read the opened csv file
    for row in csvreader:  # for each row in the csvreader
        datalist.append(row)  # appends the data in each row to empty datalist
    return datalist  # returns the datalist


def data_2011(alldata):  # Function A
    for vdata in range(1, 7):  # For data from row 1 to 7
        print(f'The number of vehicles crossed at {alldata[vdata][0]} in 2011 is {alldata[vdata][2]}')  # displays the City from column 0 within the range and the vehicle data from column 2
        #t.sleep(1)

def data_mean(alldata):  # Function B
    vdata = []  # Creates empty datalist for storage of required vehicle data
    ydata = []  # Creates empty datalist for storage of required year data
    mean = 0.0  # initialize mean to zero
    print('=' * 100)  # Display Menu
    print('''Please select a city
    Anacortes - 1
    Boundary - 2
    Danville - 3
    Frontier - 4
    Laurier - 5
    Port Angeles - 6''')
    print('=' * 100)
    selectedCity = int(input('Please enter the City of your choice '))  # prompts user for input and converts it into an integer
    for year in range(1, 7):  # for all data between 2010 and 2015
        ydata.append(alldata[0][year])  # Appends data from csv file in row 0 into ydata list
    for row in range(1, 7):  # for all data between 2010 and 2015
        vdata.append(int(alldata[selectedCity][row]))# Appends data in the form of integers in range from csv file(alldata) in the selectedCity(row number) into vdata list
        mean = sum(vdata) / 6  # Calculates mean

    print(f'The mean is {mean:.2f} in the 6-year span of 2010 to 2015')  # Displays the mean
    for val in range(0, 6):  # for all the values within range(0 to 6 now because your index one appended becomes index 0 in new list)
        if vdata[val] > mean:  # Compares values to the mean
            print(f'The year that exceed the mean is {ydata[val]} and the mean is {vdata[val]}')  # Displays the values that exceed the mean and their years
            #t.sleep(1)

def FunctionC(alldata):  # Function C
    vdata = []  # Creates empty datalist for storage of required vehicle data
    ydata = []  # Creates empty datalist for storage of required year data
    print('=' * 100)  # Display Menu
    print('''Please select a city
        Anacortes - 1
        Boundary - 2
        Danville - 3
        Frontier - 4
        Laurier - 5
        Port Angeles - 6''')
    print('=' * 100)
    selectedCity = int(input('Please enter your city of choice:'))  # Prompts user for input and converts it into an integer
    for row in range(1, 11):  # For all the values between 2010 and 2019(inclusive of 2019)
        vdata.append(int(alldata[selectedCity][row]))  # Appends all values in range from the selectedCity(row number) into vdata list
        ydata.append(alldata[0][row])  # Appends all year values from alldata in row 0 into ydata list
    for val in range(1, 10):  # For values in this range
        if -((vdata[val] - vdata[val - 1]) / vdata[val - 1] * 100) >= 5:  # -(Present year - Previous year / Previous year)*100% = percentage difference.Compare percentage difference to 5%
            print(f'The value that has decreased by at least 5% is {vdata[val]} and occurred in the year {ydata[val]}')  # Displays the value which has decreased by at least 5% and displays the year
            t.sleep(1)
        else:
            print(f'The value has not decreased by at least 5% in {ydata[val]}')  # Displays the year iin which the value has not decreased by at least 5%
            #t.sleep(1)

def FunctionD(alldata):  # Function D
    Dvdata = []  # Creates empty datalist for storage of Danville vehicle data
    Fvdata = []  # Creates empty datalist for storage of Frontier vehicle data
    Bvdata = []  # Creates empty datalist for storage of Boundary vehicle data
    Pvdata = []  # Creates empty datalist for storage of Port Angeles vehicle data
    ydata = []  # Creates empty datalist for storage of required year data
    for row in range(1, 11):  # For all the values between 2010 and 2019(inclusive of 2019)
        Dvdata.append(int(alldata[3][row]))  # Appends Danville vehicle data to respective data list
        Fvdata.append(int(alldata[4][row]))  # Appends Frontier vehicle data to respective data list
        Bvdata.append(int(alldata[2][row]))  # Appends Boundary vehicle data to respective data list
        Pvdata.append(int(alldata[6][row]))  # Appends Port Angeles vehicle data to respective data list
        ydata.append(int(alldata[0][row]))  # Appends year data to respective data list
    loop = True  # Sets loop to True
    while loop:  # while loop = True
        print('=' * 100)  # Displays Menu
        print('''Please select an option
         1 - Line graph
         2 - Bar graph
         3 - Quit
         ''')
        print('=' * 100)
        selectedPlot = input('Please enter your plot of choice:')  # Prompts user for selection
        if selectedPlot == '1':  # If 1 is selected
            plt.plot(ydata, Dvdata, label='Danville ')  # Plots a line graph of Danville against the year
            plt.plot(ydata, Fvdata, label='Frontier')  # Plots a line graph of Frontier against the year
            plt.title("Number of vehicle crossings from Danville and Frontier (in each year) vs Year ")  # Plot title
            plt.legend() # Plot legend
            plt.xticks(ydata) # Shows all x-axis values
            plt.show()  # Displays the plot
        elif selectedPlot == '2':  # If 2 is selected
            x_axis = np.arange(len(ydata))  # Generates an array of values in intervals of 1 in range of the length of ydata list
            plt.bar(x_axis + 0.2, Bvdata, width=0.4, label='Boundary')  # Plots a bar graph of Boundary against the year
            plt.bar(x_axis - 0.2, Pvdata, width=0.4, label='Port Angeles')  # Plots a bar graph of Port Angeles against the year
            plt.title("Number of vehicle crossings from Boundary and Port Angel (in each year) vs Year ")  # Plot title
            plt.legend(loc='lower left') # Plot legend
            plt.xticks(x_axis, ydata)  # Shows all x-axis values with x_axis indicating positions of the ticks and ydata indicating the labels of the respective ticks
            plt.show()  # Displays the plot
        elif selectedPlot == '3':  # If 3 is selected
            loop = False  # Breaks the loop
        else:
            print('Invalid Selection')  # prints statement and continues loop
