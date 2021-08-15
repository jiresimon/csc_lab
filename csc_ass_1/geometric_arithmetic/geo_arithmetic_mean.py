from math import *
print("Program to calculate the geometric/arithmetic mean of a set of positive values")
print()
print("N -- Total number of positive values given")
print()

total_num = int(input("Enter the value for 'N' in the question:\n>>> "))
print()

print("Press the ENTER KEY to save each value you enter...")

i = 1
num_list = []

while  (i <= total_num):

    numbers = int(input("Enter the numbers:\n>>> "))
    if numbers > 0 :
        num_list.append(numbers)
    elif numbers < 0:
        break
        
    i+=1

#To calculate the geometric mean
try:
    geo_mean_1 = prod(num_list)
    geo_mean_2= pow(geo_mean_1, 1/total_num)

    #To calculate the arithmetic mean
    ar_mean_1 = sum(num_list)
    ar_mean_2 = (ar_mean_1/len(num_list))
    
    print('Here are your answers...')
    print()
    print(f"The geometric mean of the given set of positive values is {geo_mean_2}")
    print(f"The arithmetic mean of the given set of positive values is {ar_mean_2}")

except ZeroDivisionError:
    print("Not divisible by zero")




    
