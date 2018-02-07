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
    
    def __init__(self, numCols, numRows):
        self.numCols = numCols
        self.numRows = numRows
        self.position = []
    
    #Determines if a matrix is square. Returns a boolean
    def _isSquare(self):
        return (self.numCols == self.numRows)
    
    #Determines if two matricies can be multiplied. Returns a boolean
    def _canMulti(self, matrx):
        return (self.numRows == matrx.numCols) and (self.numCols == matrx.numRows)
    
    #Determines if two matricies can have arithmatic performed
    #  on them. Returns a boolean
    def _canArith(self, matrx):
        return (self.numCols == matrx.numCols) and (self.numRows == matrx.numRows)
    
    """
    initMatrix is a method that returns nothing and has the
    side effect of initializing the position instance variable
    of the matrix it is called on. 
    It takes no arguments, and instead prompts the user
    for the correct number of values (based on numCols and
    numRows).
    """
    def initMatrix(self):
        #double map float onto matrix?
        for r in range(self.numRows):
            layer = []
            for c in range(self.numCols):
              layer.append(float(input("Input value for [" + r + "," + c +"] :")))
            self.position.append(layer)
                      
    """
    det calculates and returns the determinant of the matrix
    if possible. If not possible, it prints an error message.
    """
    def det(self):
        #a guard to ensure that matrix is square and thus has a determinant
        if(not self._isSquare()):
            print("Given matrix is not square, cannot compute determinant")
        else:
            """
            recursive, with 2x2 base case
            1st col becomes multiplier column
            
            *creat a for loop with a sign = 1 and at end of every
             for loop mulitpy sign by -1 so as to maintain
             the correct signage on the multiplied matricies?
            
            """
            
            return 0
    
    
    
    
    
    
    
    