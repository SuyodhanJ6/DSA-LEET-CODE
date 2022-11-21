class Solution:
    """
    This class help to find the solution.
    """
    def runningSum(self, nums):
        """
        Method Name : runningSum
        Description : This help to finding the sum of array at running.
        Output      : Array
        On Failure  : None
        """
        
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums
nums = [1,2,3]
s = Solution()
s.runningSum(nums)