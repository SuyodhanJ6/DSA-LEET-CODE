class Solution:
    '''
    this method finding the solution by using method.
    '''
    def buildArray(self, nums):
        
        '''
        Method Name : buildArray
        Description : This method using permutation combination building array with the help of some
                        basic statements.
        Output      : Array
        On Failure : None
        '''
        
        n = len(nums)
        for i in range(n):
            a = nums[i]
            
            b = (nums[nums[i]]) % n
            nums[i] = a + b*n
            
        for i in range(n):
            nums[i] = nums[i] // n
        return nums
nums= [0,2,1,5,3,4]
s = Solution()
s.buildArray(nums)