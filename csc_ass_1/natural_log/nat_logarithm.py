from math import *
def natural_logarithm():
    '''Program calculates the natural logarithm of valid values of x (numbers)'''
    
    x = int(input("Enter the value of x:\n>>> "))
    logarithm = True

    try:
        while logarithm:
            if x < 0:
                log_cal = log(1/(1-x))
                print(f"Ans: {log_cal}")

                natural_logarithm()
                break

            elif x > 0:
                break
            
            else:
                print("Invalid Input")
                break

    except ValueError:
        print("Invalid Input")
    
natural_logarithm()


