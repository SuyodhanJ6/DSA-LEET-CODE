from itertools import count


class Solution:
    def __init__(self):
        pass
    
    def numIdenticalPairs(self, nums):
        """
        Method Name : numIdenticalPairs
        Description : This method help to count the identical pairs from the list.
        OutPut      : Int
        On Failure  : None
        """
        my_count = 0
        my_dict = {}
        
        for i in nums:
            if i in my_dict:
                # Increasing count
                my_count += my_dict[i]
                # Increasing dict value after accruing same value so increase the count in the dict
                my_dict[i] += 1

            else:
                # So value is first time in the dict so count is 1 always.
                my_dict[i]  = 1
        return my_count
        
            
# Driver Code
nums = [1,2,1,2]
s = Solution()
print(s.numIdenticalPairs(nums))
