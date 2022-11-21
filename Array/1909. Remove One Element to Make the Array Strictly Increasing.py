from operator import index
from os import remove


class Solution:
    ''' this class finding the solution. '''
    
    def canBeIncreasing(self,nums):
        '''
        Method Name : canBeIncreasing
        Description : This method find the number is greater than the previous number
                        then number deleting and return True
        Output      : True Or False(boolean)
        On Failure  : None
        
        '''
        # Count the increasing element in the array
        n = len(nums)
        index = -1
        count = 0
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                index = i
                count += 1
        
        if count == 0:
            return True
        if count == 1:
            if index == 0 or index == n-2:
                return True
            if nums[index-1] < nums[index + 1] or (index+2 and nums[index] < nums[index+2]):
                return True
        return False
        
                
        

nums = [1,2,10,5,7]
    
s = Solution()
s.canBeIncreasing(nums)