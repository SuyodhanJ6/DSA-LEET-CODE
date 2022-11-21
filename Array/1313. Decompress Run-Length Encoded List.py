class Solution:
    def __init__(self):
        pass
    
    def decompressRLElist(self, nums):
        """
        Method Name   : decompressRLElist
        Description   : In this method we considering pair of tuple or list the consider the first is freq and the second one is val so
                        use extend method iterable the element rage of freq not overloading
        Output        : Array
        On Failure    : None
        """
        
        l = len(nums)
        list = []
        for i in range(0, l, 2):
            list.extend(nums[i] * [nums[i+1]]) # Okay Here nums[i] times element is iterable
        return list

nums = [1,2,3,4]
s = Solution()
print(s.decompressRLElist(nums))