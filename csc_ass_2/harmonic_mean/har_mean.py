print("Program to calculate the harmonic mean of a set of positive values")
print()

print("N -- Total number of positive values given")
print()

def harmonic_mean():
    '''Program calculates the harmonic mean of positive values of x'''
    
    total_num = int(input("Enter the value for 'N' in the question:\n>>> "))
    print()

    print("Press the ENTER KEY to save every value of 'X' you enter...")

    #creating a while loop to read in the input values
    i = 1
    num_list = []

    while  (i <= total_num):
        try: 
            numbers = int(input("Enter the numbers:\n>>> "))
            
            if numbers > 0 :
                num_list.append(numbers)
            elif numbers < 0:
                break
               
            i+=1
        
        except ValueError:
            return "Invalid Input"

    #mathematical calculation
    #create a for loop for the sum of inverse of every value of x
    sum_inverse_numbers = 0
    for X in num_list:
        sum_inverse_numbers = sum_inverse_numbers + 1/X

    #harmonic mean formula
    try:
        harm_mean = len(num_list) / sum_inverse_numbers
        return f"The harmonic mean result = {harm_mean}"

    except ZeroDivisionError:
        return "Invalid division with zero"

harmonic_mean_result = harmonic_mean()
print(harmonic_mean_result)