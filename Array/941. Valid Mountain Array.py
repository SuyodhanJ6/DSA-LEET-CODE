class Solution:
    def __init__(self):
        pass
    
    def validMountainArray(self, arr):
        """
        Method Name     :  validMountainArray
        Description     : Given an array of integers arr, return true if and only if it is a valid mountain array.
        OutPut          : Boolean
        On Failure      : None
        """
        l = 0 # left pointer
        r = len(arr) -1  #right pointer
        # arr.length >= 3
        if len(arr) == 0 or len(arr) == 1:
            return False
        while l + 1 < len(arr) -1 and arr[l] < arr[l+1]:
            l += 1
        while r - 1 > 0 and arr[r] < arr[r-1] :
            r -= 1
        return l == r
# Driver Code
arr = [2]
s = Solution()
print(s.validMountainArray(arr))
        