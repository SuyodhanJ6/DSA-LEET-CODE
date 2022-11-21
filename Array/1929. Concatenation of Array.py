class Solution:
    """
    this class is used for finding the solution'
    """
    
    def getConcatenation(self, nums):
        """
        Method Name : getConcatenation
        Description : This method help to concatenation two array in a single array.
        Output      : Array
        On Failure  : None
        """
        
        n = len(nums)
        for i in range(n):
            a = nums[i]
            nums.append(a)
        return nums
nums = [1,2,3]
s =Solution()
s.getConcatenation(nums)