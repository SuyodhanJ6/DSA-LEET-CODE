from operator import le


class Solution:
    """
    This class help to finding the solution.
    """
    def finalValueAfterOperations(self, operation):
        """
        Method Name : finalValueAfterOperations
        Description : This method help to find the operation and perform increment and decrement operation in the above code
        Output      : int
        On Failure  : None
        """
        
        a = self.operation.count("X++") 
        b = self.operation.count("++X")
        c = self.operation.count("--X")
        d = self.operation.count("X--")
    
        return a + b - c - d
            
        """
        dict = { 'X'++ : 1 , '++X' : 1, 'X--' : -1, '--X' : -1}
        for i in operation:
            a = sum(dict(i)) 
        return a 
        
        """        