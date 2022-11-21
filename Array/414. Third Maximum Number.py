class Solution:
    def __init__(self):
        pass
    
    def thirdMax(self, nums):
        """
        MEthod Name   : thirdMax
        Description   : Given an integer array nums, return the third distinct maximum number in 
                        this array. If the third maximum does not exist, return the maximum number. 
        Output        : Boolean
        OnFailure     : None
        """
        l = list(set(nums))
        l.sort()
        if len(l) <= 2:
            return l[-1]
        else:
            return l[-3]
    
# Driver Code
nums = [3,2,1]
s = Solution()
print(s.thirdMax(nums))
        