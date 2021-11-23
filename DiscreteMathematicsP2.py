#Imports
import numpy as np

def solveEquation(v0, g, t):
    """

    This function will calculate the mathematical equation 
    that represents an object in vertical movement.

    y(t) = v0t-(1/2)gt**2

    y-height(position) as a function of time t
    v0-initial speed at t=0
    g-gravity acceleration
    t-time

    """
    result = v0*t-(1/2)*g*t**2
    return print("Result of the equation: ", np.round(result,decimals=2))

class negativeValue(Exception):
    pass

#Creating 'menu' array
menu = {}

menu['a']="Mathematical Equation - Free Fall"
menu['b']="2D Graph"
menu['c']="3D Graph - plot_trisurf"
menu['d']="Exit"

while True:

    #Getting all keys of the menu array
    options=menu.keys()
    print("\nAll Exercises Below:")
    print("---------------------------------------------")
    #for cicle to print all menu options with respective entries(a,b,c,d)
    for entry in options:
        print(entry, menu[entry])

    #Save user selected option in variable 'selected'
    selected=input("\nPlease, select the exercise: ")

    """
    When the user input from [a-c] it will goes to the respective exercise
    If the user input is 'd' it will exit from the application
    But... when it's an different input not from [a-d] a message will be displayed
    """

    #Exercise a - Mathematical Equation
    if selected == 'a':
        print("\nExercise a - Mathematical Equation")
        print("---------------------------------------------")
        while True:

            try:
                v0 = float(input("Insert initial speed(v0): "))
                g = float(input("Insert gravity acceleration(g): "))
                t = float(input("Insert time(t): "))
                                
                if v0 < 0 or g < 0 or t < 0:
                    raise ValueError

            except ValueError:            
                print("Please, insert only positive numbers.")
            else:
                solveEquation(v0,g,t)
                break 
                
    elif selected == 'b':
        print("Exercise b - 2D Graph")
        print("---------------------------------------------")
    
    elif selected == 'c':
        print("Exercise c - 3D Graph")
        print("---------------------------------------------")
   
    elif selected == 'd':
        break
    
    else: 
        print("\nInvalid Option Selected!")

