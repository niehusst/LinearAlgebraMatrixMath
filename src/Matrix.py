#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sympy import solve, evalf
from re import match

"""
This Matrix class helps with computational linear algebra,
as well as other basic matrix math procedures.
(Note that this is by no means the most efficient program
possible; it uses cofactor expansion (as opposed to elementary 
operations) to do determinant computations, slowing
computation in the affected methods for larger matrices by 
a factor of O(n!). While these methods function for matrices
of any size, they unsatifactory runtimes for matricies 
larger than 9x9.)
All methods are intended to accomodate only real numbers.

Required fields for instantiation are numRows and numCols.
The position field is optional.

@author Liam Niehus-Staab
@since Feb 1, 2018
*******************************
***Fields of Matrix instance***
* 0. numRows                  *
* 1. numCols                  *
* 2. position                 *
**public Matrix class methods**
* 0. initMatrix               *
* 1. det                      *
* 2. inverse                  *
* 3. eigenVals                *
* 4. times                    *
* 5. plus                     *
* 6. minus                    *
* 7. printM                   *
**private Matrix class methods*
* 0. _isSquare                *
* 1. _canMulti                *
* 2. _canArith                *
* 3. _subMatrix               *
* 4. _scalarMulti             *
* 5. _matrixMulti             *
* 6. _cofactor                *
* 7. _transpose               *
* 8. _inverseKernel           *
* 9. _lambdaMatrix            *
* 10. _stringDet              *
* 11. _stringTimes            *
*******************************
"""

class Matrix(object):
    
    """
    The constructor of the Matrix class. Requires that the
    desired dimensions of the matrix be given at instantiation
    and initialization to occur at a later date.
    
    @param numCols - an int number of columns the Matrix will have.
    @param numRows - an int number of rows the Matrix will have.
    @param position - A list of lists. The numeric data 
                      contained in the Matrix object. (optional)
    """
    def __init__(self, numRows, numCols, position=[]):
        self.numCols = numCols
        self.numRows = numRows
        self.position = position
    
    ########## PRIVATE METHODS ##########
    """
    Determines if a matrix is square. 
    
    @return - a boolean, <true> if self has the same number of
              rows as columns, else <false>.
    """
    def _isSquare(self):
        return (self.numCols == self.numRows)
    
    """
    Determines if two matricies can be multiplied together.
    
    @param matrx - A Matrix type object.
    @return - a boolean, <true> if self has same number of 
              columns as matrx has rows. Else, <false>.
    """
    def _canMulti(self, matrx):
        return (self.numCols == matrx.numRows) 
    
    """
    Determines if two matricies can be arithmatically compared
    to each other.
    
    @param matrx - a Matrix type object
    @return - a boolean, <true> if self and matrx have the
              same dimensions, else <false>
    """
    def _canArith(self, matrx):
        return (self.numCols == matrx.numCols) and (self.numRows == matrx.numRows)
    
    """
    Creates and returns a square matrix that is a piece of the
    larger matrix, self. The new Matrix excludes the first 
    column, and the specified row. A helper for the det and 
    inverse methods.
    
    @param notRow - An integer that is less than self.numRows
                    and indicates which row not to include in result.
    @param notCol - An integer that is less than self.numCols
                    and indicates which column not to include in
                    the result.
    @return - A square Matrix object which is smaller by 1 dimension
              than the original object.        
    """
    def _subMatrix(self, notRow, notCol):
        newMatrix = []
        for row in range(self.numRows):
            newRow = []
            if(row != notRow):
                for col in range(self.numCols):
                    if(col != notCol):
                        newRow.append(self.position[row][col])
                newMatrix.append(newRow)
        return Matrix(self.numRows-1, self.numCols-1, newMatrix)
    
    """
    A method to multiply a scalar, real number with the Matrix
    object, self.
    
    @param operand - a real number
    @return m - a Matrix type object
    """
    def _scalarMulti(self, operand):
        matrx = []
        for row in self.position:
            newRow = []
            for val in row:
                newRow.append(val * operand)
            matrx.append(newRow)
        return Matrix(self.numRows, self.numCols, matrx)
    
    """
    A method for multiplying two Matrix objects together.
    
    @param operand - a Matrix object
    @return - a Matrix object (the product)
    """
    def _matrixMulti(self, operand):
        matrx = []
        for row in range(self.numRows):
            newRow = []
            for col in range(operand.numCols):
                val = 0
                for x in range(self.numCols):
                    val += self.position[row][x] * operand.position[x][col]
                newRow.append(val)
            matrx.append(newRow)
        return Matrix(self.numRows, operand.numCols, matrx)
    
    """
    A method for creaing a matrix of CoFactors from the
    Matrix object, self. This is done by making the matrix
    of minors and signing each element as it put into the
    matrix. A helper for the inverse method.
    
    @return - a Matrix object, the matrix of cofactors
    """
    def _cofactor(self):
        sign = 1
        matrx = []
        for row in range(self.numRows):
            newRow = []
            for col in range(self.numCols):
                newRow.append(sign * (self._subMatrix(row, col)).det())
                sign *= -1
            sign *= -1
            matrx.append(newRow)
        return Matrix(self.numRows, self.numCols, matrx)
    
    """
    A method to return the transposition of self.
    A helper for the inverse method.
    
    @return - a Matrix object, the transpose of self.
    """
    def _transpose(self):
        matrx = []
        for row in range(self.numRows):
            newRow = []
            for col in range(self.numCols):
                newRow.append(self.position[col][row])
            matrx.append(newRow)
        return Matrix(self.numRows, self.numCols, matrx)
        
    """
    The kernel of the public wrapper method inverse.
    This method handles the actual computation of the
    matrix inverse by finding the cofactor of the matrix
    of minors, and then transposing it; resulting in the
    adjugate matrix. And the inverse is calculating by 
    mulitplying the adjugate by the inverse determinant.
    
    @param determinant - a float, the determinant of self.
    @return - a Matrix object, the inverse of self.
    """
    def _inverseKernel(self, determinant):
        #Special case of the 1x1 matrix
        if(self.numRows == 1 and self.numCols == 1):
            return Matrix(1, 1, [[1.0/self.position[0][0]]])
        else:
            adjugate = self._cofactor()._transpose()
            return adjugate.times(1.0/determinant)
        
    """
    Calculates the matrix that results from (A - (lambda)I)
    where I is the identity matrix and lambda represents
    an eigenvalue. Uses Strings as elements to facilitate
    use with sympy 'solve' function.
    
    @return - a Matrix object, different from the usual Matrix
              in that its elements are all strings.
    """
    def _lambdaMatrix(self):
        matrx = []
        for row in range(self.numRows):
            newRow = []
            for col in range(self.numCols):
                if(row == col):
                    newRow.append(str(self.position[row][col]) + " - y")
                else:
                    newRow.append(str(self.position[row][col]))
            matrx.append(newRow)
        return Matrix(self.numRows, self.numCols, matrx)
    
    """
    _stringTimes is a function that takes two Strings and
    concatanates them with a '*' character in between.
    
    @param v1 - A String, should represent a real number, or
                a combination of real numbers and symbols.
    @param v2 - A String, should represent a real number, or
                a combination of real numbers and symbols.            
    @return - a String, the concatination of v1 and v2 
              seperated by "*".
    """
    def _stringTimes(self, v1, v2):
        return "(" + v1 + ") * (" + v2 + ")"
    
    """
    _stringDet converts and concatinates all of the calculations 
    of the determinant into a String and returns that String of  
    calculations if possible. If not possible, it returns an 
    error message.
    
    PRECONDITION - only Matrix objects with equal fields
                   numRows and numCols have determinants.
                   If this precondition isn't met, an error
                   String will be returned.
    
    @return d - a String, the determinant of self. 
    @return - if no determinant is possible, a String error 
              message is returned.
    
    """
    def _stringDet(self):
        sign = 1
        #a guard to ensure that matrix is square and thus has a determinant
        if(not self._isSquare()):
            return "Given matrix is not square, cannot compute determinant."
        #Special case of the 1x1 matrix whose determinant is itself
        if(self.numRows == 1 and self.numCols == 1):
            return Matrix(1,1,[[str(self.posiiton[0][0])]])
        else:
            d = ""
            #The recursive base case
            if(self.numRows == 2 and self.numCols == 2):
                
                return (self._stringTimes(self.position[0][0], self.position[1][1]) 
                        + " - " + self._stringTimes(self.position[0][1], self.position[1][0]))
            else:
                for row in range(self.numRows):
                    coef = self._stringTimes(str(sign), self.position[row][0])
                    d += self._stringTimes(coef, (self._subMatrix(row,0))._stringDet()) + " + "
                    sign *= -1
                d += "0"
                return d
    
    ########## PUBLIC METHODS ###########
    """
    initMatrix is a method that returns nothing and has the
    side effect of initializing the position instance variable
    of the matrix it is called on. 
    
    It takes no arguments, and instead prompts the user
    for the correct number of values (based on self.numCols and
    self.numRows).
    """
    def initMatrix(self):
        matrx = []
        for r in range(self.numRows):
            newRow = []
            for c in range(self.numCols):
              newRow.append((float(input("Input value for ["
                           + str(r) + "," + str(c) +"]: "))))
            matrx.append(newRow)
        self.position = matrx
                      
    """
    A function to print a Matrix type object in a more
    readable fashion.
    """
    def printM(self):
        for row in self.position:
            print(row)
    
    """
    times, A method to multiply the self with operand. Works
    with both real (float and int) and Matrix types. 
    
    @param operand - Either a real number or a matrix of legal
                     dimensions.
    @return - A new Matrix object.
    @return - An error String in the case of invalid input
    """
    def times(self, operand):
        if(isinstance(operand, int) or isinstance(operand, float)):
            return self._scalarMulti(operand)
        elif(isinstance(operand, Matrix) and self._canMulti(operand)):
            return self._matrixMulti(operand)
        else:
            return "Illegal operand error."
            
    """
    plus, A method to add the self with operand.
    
    @param operand - A matrix of legal dimensions.
    @return - A new Matrix object.
    """
    def plus(self, operand):
        if(self._canArith(operand)):
            matrx = []
            for row in range(self.numRows):
                newRow = []
                for col in range(self.numCols):
                    newRow.append(self.position[row][col] + operand.position[row][col])
                matrx.append(newRow)
            return Matrix(self.numRows, self.numCols, matrx)
        else:
            return "Illegal operand error."
        
    """
    minus, A method to subtract the operand from self.
    
    @param operand - A matrix of legal dimensions.
    @return - A new Matrix object.
    """
    def minus(self, operand):
        if(self._canArith(operand)):
            matrx = []
            for row in range(self.numRows):
                newRow = []
                for col in range(self.numCols):
                    newRow.append(self.position[row][col] - operand.position[row][col])
                matrx.append(newRow)
            return Matrix(self.numRows, self.numCols, matrx)
        else:
            return "Illegal operand error."
        
    """
    det calculates and returns the determinant of the Matrix
    if possible. If not possible, it returns an error message.
    
    PRECONDITION - only Matrix objects with equal fields
                   numRows and numCols have determinants.
                   If this precondition isn't met, an error
                   String will be returned.
    
    @return d - The determinant of self, a real number. 
    @return - if no determinant is possible, a String error 
              message is returned.
    """
    def det(self):
        sign = 1
        #a guard to ensure that matrix is square and thus has a determinant
        if(not self._isSquare()):
            return "Given matrix is not square, cannot compute determinant."
        #Special case of the 1x1 matrix whose determinant is itself
        if(self.numRows == 1 and self.numCols == 1):
            return self.position[0][0]
        else:
            d = 0.0
            #The recursive base case
            if(self.numRows == 2 and self.numCols == 2):
                return (self.position[0][0] * self.position[1][1] 
                        - self.position[0][1] * self.position[1][0])
            else:
                for row in range(self.numRows):
                    coef = sign * self.position[row][0]
                    d += coef * (self._subMatrix(row,0)).det()
                    sign *= -1
                return d
    
    """
    A method to calculate and return the inverse of the Matrix object,
    self, by finding its adjugate, and then multiplying it by 
    the inverse of the determinant. THIS IS A VERY COMPUTATIONALLY
    COSTLY METHOD.
    
    PRECONDITION - only Matrix objects with equal fields
                   numRows and numCols have determinants (and
                   thus inverses), and only matricies with non-zero
                   determinants have inverses.
                   If this precondition isn't met, an error
                   String will be returned.

    @return - a Matrix object, the inverse matrix of self.
    @return - a String, reports the type of error that was 
              encountered (non-square matrix or self.det() == 0)
    """
    def inverse(self):
        #guards against illegal matrix input
        if(not self._isSquare()):
            return "Illegal matrix dimensions, self isn't square."
        #store the value of the determinant to save costly computation
        determinant = self.det()
        if(determinant == 0):
            return "Determinant of 0, no inverse."
        else:
            return self._inverseKernel(determinant)
        
    """
    This method finds the eigenvalues of a Matrix object,
    if they exist. Some eigenvalues may be complex, this
    method returns only the real portion of those complex 
    numbers.
    
    @return - a list, contains the real eigenvales of the 
              matrix as floats, or complex numbers.
    @return - a String, in the event that there are no eigenvalues
    """
    def eigenVals(self):
        #y = Symbol('y') #give back to lambdaMatix
        if(not self._isSquare):
            return "Eigenvalues don't exist for non-square matrix."
        else:
            charPoly = self._lambdaMatrix()._stringDet()
            eigens = solve(charPoly)
            return eigens
    

    
    