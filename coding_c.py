import sys 
import pandas as pd
import numpy as np
 

#name = sys.stdin.readline() 
#print(name) 

######################################

#Read a list of numbers
#Test with example

#1, 2, 3, 137.036
ex = [1, 2, 3, 137.036]
ex

######################################
#Check if a list is empty or count elements in list

numlist = []

def fill_list(num1):
    if num1:
        print("This list has", len(num1), "elements")
    else:
        print("The list is empty")
        
        
fill_list(numlist)

#############################

# Define the function get the median
def get_med(list1):
    """Get the Median of a list """
    list1.sort() 
    mid = len(list1) // 2
    res = (list1[mid] + list1[~mid]) / 2
    return round(res,3)

print(get_med(ex),type(get_med(ex)))

#############################

# Define the function get the mean
def get_mean(list1):
    """Get the mean of list  """
    #print(sum(list1)/len(list1))
    res = sum(list1)/len(list1)
    return round(res,3)

print(get_mean(ex),type(get_mean(ex)))

#############################

# Define the function get the mean
def get_stdev(list1):
    """Get the standard deviation of list  """
    var = sum((x - (sum(list1)/len(list1))) ** 2 for x in list1) / len(list1)
    res = var**(0.5)
    return round(res,3)

 
print(get_stdev(ex),type(get_stdev(ex)))

#############################

#Determine if a input string is a numeric or not
def get_number(x):
    """Determine if the input variable is a numeric   """
    try:
        float(x)
        return True
    except ValueError:
        return False

#############################

i=0
i2 =[]
while True:
    #print(i)
    #print(i2)
    fill_list(i2)
    
    print('----------------------')

    #num7 = input("Enter any number, to exit press a non numeric key and 'enter'): ")
    print("Enter any number, to exit press a non numeric key and 'enter': ")
    num9 = sys.stdin.readline() 
    num7=num9
    num7 =num7.upper()
    print(type(num7),'Type String')
    
    if num7 == 'EXIT' :
        print(num7, 'time to stop')
        break
    
    elif get_number(num7) == False:
        print(num7, 'time to stop')
        break
    elif type(num7) == complex:
        print('Complex Number, use integers and floats please')
        break
    else:
 
        num2=num7
      
        i2.append(float(num2))
        #print("number is: ", num2)
        
        print(' \n')
        print(get_mean(i2),get_stdev(i2),get_med(i2))
        print(' \n')
        
        #i=i+1
        #if i == 7:
        #    break
    

#############################

print("\n Exiting Program") 
#############################


#############################

    
#print('To quit type lowercase q');

#for num8 in sys.stdin: 
#    if 'q' == num8.rstrip(): 
#        break
#    print(f'Input : {num8}') 

#############################


#############################


#############################


