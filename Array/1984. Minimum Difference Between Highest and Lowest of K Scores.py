class Solution:
    """
    This class help to find the solution.
    """
    def minimumDifference(self, nums, k):
        """
        Method Name : minimumDifference
        Description : This function help to find out the min diff between highest num and lowest num.
        Output      : int 
        On Failure  : None
        """
        nums.sort()
        if len(nums) <= 1:
            return 0
        
        l, r = 0, k-1
        minDiff = float("inf")
        while r < len(nums):
            minDiff = min(minDiff, nums[r]- nums[l])
            l, r = l+1, r+1
        return minDiff
    
# Driver Code
nums = [9,4,1,7]
k = 2
s = Solution()
print(s.minimumDifference(nums, k))
            