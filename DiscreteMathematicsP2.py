#Imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas as pan


"""
FUNCTIONS
"""
def colored(r, g, b, text):

    """
    This function will colored the print message with the pretended color.
    The objetive of it is to define the type of printed message (SUCCESS, ERROR, WARNING, etc.).
    """

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

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
    ax.set_title("Variation of y in a Time Interval", fontweight='bold')
    ax.legend(['y(t)'])
    ax.set_xlabel("Time interval(t)", fontweight='bold')
    ax.set_ylabel("Height(y)", fontweight='bold')
    
    #Show the plot
    plt.show()

def build3DGraph(x,y,z):

    """
    This function will generate the 3D graph using plot_trisurf 
    that generates a Tri-Surface Plot (created by triangulation of compact surfaces of finite number of triangles).
    This method have as a paramaters the X,Y and Z axis.
    """

    #Creating a new figure
    fig = plt.figure(figsize=(16,9))
    
    #Adding axes to the current figure and make it the current axes
    #In this case 3D axes object
    ax = plt.axes(projection="3d")
        
    #Creating plot
    trisurf = ax.plot_trisurf(x,y,z,
                            cmap=cm.hot,
                            linewidth = 0.0, 
                            antialiased=True,
                            edgecolor='grey')

    #Add a color bar corresponding to the values
    fig.colorbar(trisurf,ax=ax, shrink=0.5, aspect=5)

    #Set a title
    ax.set_title('Tri-surface plot', fontweight='bold')

    #Add labels
    ax.set_xlabel('X-axis', fontweight='bold')
    ax.set_ylabel('Y-axis', fontweight='bold')
    ax.set_zlabel('Z-axis', fontweight='bold')  

    #Show the plot
    plt.show()                        
    
"""
CUSTOM EXCEPTIONS
"""
#Exception for time interval 
class IntervalError(Exception):
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
                print(colored(255,0,0,"ERROR:"),"only positive numbers are accepted.")
                print()
            else:
                solveEquation(v0,g,t)
                print(colored(0,255,0,"SUCCESS!"),"Mathematical equation solved.")
                print()
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

                if v0 < 0 or g < 0 or initialTime < 0 or finalTime < 0:
                    raise ValueError

                if(finalTime <= initialTime):
                    raise IntervalError

            except ValueError:
                print(colored(255,0,0,"ERROR:"), "only positive numbers are accepted.")
                print()
            except IntervalError:
                print(colored(255,0,0,"ERROR:"), "final time must be higher than initial time.")
                print()
            else:
                build2DGraph(v0,g,initialTime,finalTime)
                print(colored(0,255,0,"SUCCESS!"),"2D graph generated.")
                print()
                break

    elif selected == 'c':
        print("\nExercise c - 3D Graph")
        print("---------------------------------------------")

        while True:
            try:

                #Read csv file 'data.csv' only 3 first columns with respective names: 'x','y','z' and warn that have no headers
                df = pan.read_csv('data.csv', names=['x','y','z'],header=None,usecols=[0,1,2])
                    
                x=df["x"]
                y=df["y"]
                z=df["z"]

            except FileNotFoundError:
                print(colored(255,0,0,"ERROR:"),".csv File not found.")
                print()
                break
            else:
                build3DGraph(x,y,z)
                print(colored(0,255,0,"SUCCESS!"),"3D graph generated.")
                print()
                break

    elif selected == 'd':
        break
    
    else: 
        print(colored(255,0,0,"ERROR:"),"invalid selected option.")
        print()


