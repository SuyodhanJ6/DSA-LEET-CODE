# Time Complexity : O(n)
# Space Complexity: O(n)
from collections import Counter
from math import gcd
class Solution:
    def __init__(self):
        pass
    
    def hasGroupsSizeX(self, deck):
        """
        MEthod Name   : hasGroupsSizeX
        Description   : In above method are grouping element but element present twice 
        Output        : Boolean
        OnFailure     : None
        """
        cnt_set = set(Counter(deck).values())
        gcd_val = next(iter(cnt_set))
        
        # 2, 3. Use gcd to check, return result
        for cnt in cnt_set:
            gcd_val = gcd(gcd_val, cnt)
            if gcd_val == 1: 
                return False
        return True
            
        
        
        
#Driver Code
deck = [1,1,1,2,2,2,3,3]
s = Solution()
print(s.hasGroupsSizeX(deck))