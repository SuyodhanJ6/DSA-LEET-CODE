class Solution:
    """
    This class help to the finding the solution.
    """
    
    def shuffle(self, nums, n):
        """
        Method Name : shuffle
        Description : This method helps to shuffling a array with given breakpoint n number
        Output      : Array
        On Failure  : None 
        """
        
        res = []
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]
            # print(i, j, end=" ")
            # # print(j)
        print(res)
        
nums = [1,1,2,2]
s = Solution()
s.shuffle(nums, 2)