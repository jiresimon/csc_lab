from math import *
def decibel_level():
    '''Program calculates the decibel level corresponding
       to the power levels between 1 and 20watts in 0.5steps'''


    print("Reference Power level = P1")
    print("Power level being measured = P2")

    #The reference power level P1 is 1watt
    P1 = 1
    P2 = 1

    #mathematical calculation
    while P2 <= 20:
        decibel_level_calc = 10 * log10(P2/P1)
        print("The decibel level of" +  " " + str(P2) + " " 
              + "watt(s)" + " " + "=====" + " " + str(decibel_level_calc) + "db")
        
        P2 = P2 + 0.5


decibel_level()

   