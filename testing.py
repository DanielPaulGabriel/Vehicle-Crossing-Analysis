import main_module as csvmodule  # cimports module file
datarows = []  # Creates empty list
loop = True   # Sets loop to true
while loop:  # While loop = True
    datarows = csvmodule.loadCSVData('data.csv')  # Loads CSV function and appends empty list
    csvmodule.showMenu() #loads menu function
    sel = input("Please select A, B, C, D or Q: " )  # Prompts user for input
    if sel == 'A' or sel == "a":  # if the user selects a
        csvmodule.data_2011(datarows)  # calls Function A
    elif sel == 'B' or sel == 'b':  # if the user selects b
        csvmodule.data_mean(datarows)  # calls Function B
    elif sel == 'C' or sel == 'c':  # if the user selects c
        csvmodule.FunctionC(datarows)  # calls function C
    elif sel == 'D' or sel == 'd':  # if the user selects d
        csvmodule.FunctionD(datarows)  # calls Function C
    elif sel == "Q" or sel == "q":  # if the user selects q
        loop = False  # sets loop to False and breaks loop
    else:
        print("Sorry invalid selection. Try again!")  # prints statement and continues loop
