"""
Class that helps with computational linear algebra.
(Note that this is by no means the most efficient program;
it uses cofactor expansion (as opposed to elementary 
operations) to do computations, so it dramatically slows
down the larger the matrix the methods are performed on.)
All methods are built to accomodate real numbers only.


@author Liam Niehus-Staab
@since Feb 1, 2018

***implement methods for :
0. initialize matrix vals    X
1. determinent,              
2. inverse,                  
3. eigenvalues and vectors,  
4. matrix multiplication,    
5. matrix add and subtract   
unique instance vars :     
1. num rows                  X
2. num cols                  X
((impliment using elementary ops or cofactor expansion?))
"""

class Matrix(object):
    
    """
    The constructor of the Matrix class. Requires that the
    desired dimensions of the matrix be given at instantiation
    and initialization to occur at a later date.
    
    @param numCols - The number of columns the matrix will have
    @param numRows - The number of rows the matrix will have
    """
    def __init__(self, numRows, numCols, position=[]):
        self.numCols = numCols
        self.numRows = numRows
        self.position = position
    
    #A macro constant required for determinant calculations
    SIGN = 1
    
    """
    Determines if a matrix is square. 
    
    @return - a boolean, <true> if self is square, else <false>
    """
    def _isSquare(self):
        return (self.numCols == self.numRows)
    
    """
    Determines if two matricies can be multiplied.
    
    @param matrx - a Matrix type object
    @return - a boolean, <true> if matricies 
    """
    def _canMulti(self, matrx):
        return (self.numRows == matrx.numCols) and (self.numCols == matrx.numRows)
    
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
    column, and the specified row.
    
    @param notRow - An integer that is less than matrx.numRows
                    and indicates which row not to include in result.
    @return - A square matrix which is smaller by 1 dimension
              than the original matrix.        
    """
    def _subMatrix(self, notRow):
        rowCount = 0
        newMatrix = []
        for row in self.position:
            newRow = []
            if(rowCount != notRow):
                for x in row:
                    if(x != 0):
                        newRow.append(x)
            newMatrix.append(newRow)
            rowCount += 1
        subM = Matrix(self.numRows-1, self.numCols-1, newMatrix)
        return subM
        
    """
    initMatrix is a method that returns nothing and has the
    side effect of initializing the position instance variable
    of the matrix it is called on. 
    It takes no arguments, and instead prompts the user
    for the correct number of values (based on numCols and
    numRows).
    """
    def initMatrix(self):
        for r in range(self.numRows):
            layer = []
            for c in range(self.numCols):
              layer.append(float(input("Input value for [" + r + "," + c +"] :")))
            self.position.append(layer)
                      
    """
    A function to print a Matrix type object in a more
    readable fashion.
    """
    def printM(self):
        for row in self.position:
            print(row)
    
    """
    det calculates and returns the determinant of the matrix
    if possible. If not possible, it prints an error message.
    
    @param sign - Either 1 or -1, determines the sign of the 
                  coeficient multiplier for matricies larger 
                  than 2x2.
    """
    def det(self, sign):
        global SIGN
        #a guard to ensure that matrix is square and thus has a determinant
        if(not self._isSquare()):
            print("Given matrix is not square, cannot compute determinant.")
            return "ERROR"
        else:
            d = 0.0
            #The recursive base case
            if(self.numRows == 2 and self.numCols == 2):
                return (self.position[0][0] * self.position[1][1] - self.position[0][1] * self.position[1][0])
            else:
                for row in range(self.numRows):
                    coef = sign * self.position[row][0]
                    d += coef * (self._subMatrix(SIGN)).det(SIGN)
                    sign *= -1
                return d
    
    
    
    
    
    
    
    
    
    