class Solution:
    def __init__(self):
        pass
    
    def checkIfExist(self, arr):
        """
        Method Name     :  checkIfExist
        Description     : Given an array arr of integers, check if there exist two indices i and j such that :
        OutPut          : Boolean
        On Failure      : None
        """
        
        possible_M = set()
        possible_N = set()
        for a in arr:
            if a in possible_M:
                return True
            if a in possible_N:
                return True
            if (a % 2 == 0):
                possible_M.add(a//2)
            possible_N.add(a*2)
        return False

#Driver Code
arr = [3,1,7,11]
s = Solution()
print(s.checkIfExist(arr))
