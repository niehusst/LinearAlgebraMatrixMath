#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Matrix import *
"""
A basic, text-based user-friendly interface for using
the Matrix class. Only the public methods of the Matrix
class are accessible through this interface.

@author Liam Niehus-Staab
@since Feb 6, 2018
"""

print("Welcome to the Matrix class user interface!")
print("(Type \"help\" to see your commmand options)")

m = Matrix(2, 2, [[1,0],[0,1]])
n = Matrix(2, 2, [[1,2],[3,4]])

           
while(True): #break out with break
    cmd = input("Command? ")
    if(cmd == "help"):
        print("Possible commands are:\n"
              "\t init        - inittialize matrix m or n\n"  
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
                break
            if(cmd2 == "n"):
                n.numRows = int(input("How many rows in matrix n? (must be an int) "))
                n.numCols = int(input("How many columns in matrix n? (must be an int) "))
                break
            else:
                print("Input did not match one of the possible options. Please try again.")
    elif(cmd == "det"):
        print("Determinant of m is " + str(m.det()))
    elif(cmd == "inverse"):
        print("Inverse of m is ")
        m.inverse().printM()
    elif(cmd == "eigenvalues"):
        print("The real eigenvalues of m are ")
        print(m.eigenVals())
    elif(cmd == "times"):
        while(True):
            cmd2 = input("Multiply m by n, or by scalar? (n/scalar) ")
            if(cmd2 == "n"):
                print("m times n = ")
                m.times(n).printM()
                break
            if(cmd2 == "scalar"):
                x = int(input("Input scalar (must be a real number) "))
                m.times(x).printM()
                break
            else:
                print("Input did not match one of the possible options. Please try again.")
    elif(cmd == "minus"):
        print("m minus n is")
        #try:
        m.minus(n).printM()
        #catch:
            
    elif(cmd == "plus"):
        print("m plus n is")
        #try
        m.plus(n).printM()
        #catch:
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
    else:#defaualt case
        print("Input did not match one of the possible options. Please try again.")
