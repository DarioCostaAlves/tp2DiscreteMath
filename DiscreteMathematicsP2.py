#Imports
import numpy as np

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
    selected=input("Please, select the exercise: ")

    """
    When the user input from [a-c] it will goes to the respective exercise
    If the user input is 'd' it will exit from the application
    But... when it's an different input not from [a-d] a message will be displayed
    """

    #Exercise a - Mathematical Equation
    if selected == 'a':
        print("Exercise a - Mathematical Equation")
        print("---------------------------------------------")
    
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

