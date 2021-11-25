#Imports
import numpy as np
import matplotlib.pyplot as plt

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

    y = v0*t-(1/2)*g*t**2
    return print("Result of the equation: ", np.round(y,decimals=2))

def build2DGraph(v0,g,it,ft):
    
    """
    This function will generate the 2D graph that represents
    the variation of y in a time interval(t)
    """

    #Time Interval -> [Initial Time - Final Time]
    ti = np.linspace(it,ft)
    
    #y(t) - free fall equation
    y = v0*ti-(1/2)*g*ti**2
    
    #Creating plot
    fig, ax = plt.subplots()
    lines = plt.plot(ti,y)

    #Naming title and labels
    ax.set_title("Variation of y in a Time Interval")
    ax.legend(("Height","dawd"))
    ax.set_xlabel("Time interval(t)")
    ax.set_ylabel("Height(y)")
    
    #show the plot
    plt.show()


    
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
        print("\nExercise b - 2D Graph")
        print("---------------------------------------------")
        
        while True:

            try:
                v0 = float(input("Insert initial speed(v0): "))
                g = float(input("Insert gravity acceleration(g): "))
                initialTime = float(input("Insert initial time interval(t): "))
                finalTime = float(input("Insert final time interval(t): "))

                if v0 < 0 or g < 0 or finalTime < 0:
                    raise ValueError

            except ValueError:
                print("Please, insert only positive numbers.")
            else:
                build2DGraph(v0,g,initialTime,finalTime)
                break

    elif selected == 'c':
        print("Exercise c - 3D Graph")
        print("---------------------------------------------")
   
    elif selected == 'd':
        break
    
    else: 
        print("\nInvalid Option Selected!")

