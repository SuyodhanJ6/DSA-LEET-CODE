class Solution:
    def __init__(self):
        pass
    
    def canPlaceFlowers(self, flowerbed, n):
        """
        Method Name     :  canPlaceFlowers
        Description     : In this method we are restoring the string using indices.
        OutPut          : string
        On Failure      : None
        """
        zeros, ans = 1, 0
        for f in flowerbed:
            if f==0:
                zeros += 1
            else:
                ans += (zeros-1)//2
                zeros = 0
        return ans + zeros // 2 >= n
        
        
#Driver Code
flowerbed = [1,0,0,0,1] 
n = 2
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
        