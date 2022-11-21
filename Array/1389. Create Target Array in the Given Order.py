class Solution:
    def __init__(self):
        pass
    
    def createTargetArray(self, nums, index):
        
        """
        Method Name   : createTargetArray       
        Description   : In this method we can have one array and another is 
                        array we can store index position element and create target array.
        Output        : Array
        On Failure    : None
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])  
        return target
    
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
s = Solution()
print(s.createTargetArray(nums, index))
