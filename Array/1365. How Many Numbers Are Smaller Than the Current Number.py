from unittest import result


class Solution:
    def __init__(self):
        pass
    
    def smallerNumbersThanCurrent(self, nums):
        """
        Method Name  : smallerNumbersThanCurrent
        Description  : This method find out the value smaller then current values how many value is present 
        OutPut       : list
        On Failure   : None
        """
        temp = sorted(nums)
        result = []
        dict  = {}
        for i in range(len(temp)):
            if temp[i] not in dict:  ## Here we use the indexing
                dict[temp[i]] = i
        for i in range(len(nums)):
            result.append(dict[nums[i]])
        return result
# Driver Code

nums = [8,1,2,2,3]
s = Solution()
print(s.smallerNumbersThanCurrent(nums))


    