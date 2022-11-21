class Solution:
    """
    This class help to find the solution.
    """
    def maximumDifference(self, nums):
        """
        Method Name : maximumDifference
        Description : This function help to find out the max diff between highest num and lowest num.
                        but condition is j > i
        Output      : int 
        On Failure  : None
        """
        
        maxDiff = -1
        minNum = nums[0]
        for i in range(len(nums)):
            maxDiff = max(maxDiff, nums[i] - minNum)
            minNum = min(minNum, nums[i])
        
        return maxDiff if maxDiff != 0 else -1
    
# Driver Code
nums = [7,1,5,4]
s = Solution()
print(s.maximumDifference(nums))