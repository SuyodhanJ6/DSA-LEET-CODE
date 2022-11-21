class Solution:
    def __init__(self):
        pass
    
    def kidsWithCandies(self, candies, extraCandies):
        """
        Method Name : kidsWithCandies
        Description : This method is help to the finding the greatest amoung all the kid in the list is present.
        OutPut      : boolean value
        On Failure   : None
        """
        ans = []
        lenOfCandies = len(candies)
        maxCandies = max(candies)
        for i in range(lenOfCandies):
            
            
            if candies[i] + extraCandies >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
# driver Code
candies = [12,1,12]
extraCandies = 10
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))

