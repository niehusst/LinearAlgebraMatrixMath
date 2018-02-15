#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Matrix import *
from math import factorial
"""
A basic, text-based user-friendly interface for using
the Matrix class. Only the public methods of the Matrix
class are accessible through this interface.
For matricies with more than 8 columns and rows, there
is a second prompt for computationally heavy methods that 
informs the user of an approximate runtime estimation.

@author Liam Niehus-Staab
@since Feb 6, 2018
"""

print("Welcome to the Matrix class user interface!")
print("(Type \"help\" to see your commmand options)")

#basic starting matrix values
m = Matrix(2, 2, [[1,0],[0,1]])
n = Matrix(2, 2, [[1,2],[3,4]])

"""
The following loop contains cascading if statements
to interpret user commands.
"""         
while(True): 

    cmd = input("Command? ")

    if(cmd == "help"):
        print("Possible commands are:\n"
              "\t init        - initialize matrix m or n\n"  
              "\t dimensions  - change dimensions of m or n\n"
              "\t det         - find the determinant of m\n"
              "\t inverse     - find the inverse of matrix m\n"
              "\t eigenvalues - find the eigenvalues of matrix m\n"
              "\t times       - multiply m by n, or a scalar\n"
              "\t plus        - add m and n together\n"
              "\t minus       - subtract n from m\n"
              "\t print       - print matrix m\n"
              "\t help        - get list of commands\n"
              "\t quit        - exit this program\n")

    elif(cmd == "init"):
        while(True):
            cmd2 = input("Which matrix do you want to init? (m/n) ")
            if(cmd2 == "m"):
                m.initMatrix()
                break
            if(cmd2 == "n"):
                n.initMatrix()
                break
            else:
                print("Input did not match one of the possible options. Please try again.")

    elif(cmd == "dimensions"):
        while(True):
            cmd2 = input("Dimensions of which matrix would you like to change? (m/n) ")
            if(cmd2 == "m"):
                m.numRows = int(input("How many rows in matrix m? (must be an int) "))
                m.numCols = int(input("How many columns in matrix m? (must be an int) "))
                print("Please initialize your new matrix.")
                m.initMatrix()
                break
            if(cmd2 == "n"):
                n.numRows = int(input("How many rows in matrix n? (must be an int) "))
                n.numCols = int(input("How many columns in matrix n? (must be an int) "))
                print("Please initialize your new matrix.")
                n.initMatrix()
                break
            else:
                print("Input did not match one of the possible options. Please try again.")

    elif(cmd == "det"):
        
        print("Determinant of m is ")
        if(m.numRows == m.numCols and m.numRows >= 9):
            print("WARNING: program may take approximately " + str(0.0000036 * factorial(m.numRows)) + " seconds to run.")
            ans = input("Do you want to continune? (y/n) ")
            if(ans == "y"):
                print(m.det())
        else:
            print(m.det())

    elif(cmd == "inverse"):
        print("Inverse of m is ")
        if(m.numRows == m.numCols and m.numRows >= 9):
            print("WARNING: program may take approximately " + str(0.000036 * factorial(m.numRows)) + " seconds to run.")
            ans = input("Do you want to continune? (y/n) ")
            if(ans == "y"):
                try:
                    m.inverse().printM()
                except AttributeError:
                    print("Not possible, matrix not square or has a determinant of 0.")
        else:
            try:
                m.inverse().printM()
            except AttributeError:
                    print("Not possible, matrix not square or has a determinant of 0.")
        
    elif(cmd == "eigenvalues"):
        print("The eigenvalues of m are ")
        if(m.numRows == m.numCols and m.numRows >= 7):
            print("WARNING: program may take approximately " + str(0.0019 * factorial(m.numRows)) + " seconds to run.")
            ans = input("Do you want to continune? (y/n) ")
            if(ans == "y"):
                print(m.eigenVals())
        else:
            print(m.eigenVals())
 
    elif(cmd == "times"):
        while(True):
            cmd2 = input("Multiply m by n, or by scalar? (n/scalar) ")
            if(cmd2 == "n"):
                print("m times n = ")
                try:
                    m.times(n).printM()
                except AttributeError:
                    print("Matrices not compatible, " + m.times(n))
                break
            if(cmd2 == "scalar"):
                x = float(input("Input scalar (must be a real number) "))
                m.times(x).printM()
                break
            else:
                print("Input did not match one of the possible options. Please try again.")

    elif(cmd == "minus"):
        print("m minus n is")
        try:
            m.minus(n).printM()
        except AttributeError:
            print(m.minus(n))
    elif(cmd == "plus"):
        print("m plus n is")
        try:
            m.plus(n).printM()
        except AttributeError:
            print(m.plus(n))
    elif(cmd == "print"):
        while(True):
            cmd2 = input("Which matrix would you like to print? (m/n) ")
            if(cmd2 == "m"):
                print("m, the " + str(m.numRows) + "x" + str(m.numCols) + " matrix:")
                m.printM()
                break
            elif(cmd2 == "n"):
                print("n, the " + str(n.numRows) + "x" + str(n.numCols) + " matrix:")
                n.printM()
                break
            else:
                print("Input did not match one of the possible options. Please try again.")
                
    elif(cmd == "quit"):
        print("Exiting program.")
        break
    
    else:#invalid input case
        print("Input did not match one of the possible options. Please try again.")
