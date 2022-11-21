from cmath import inf


class Solution:
    def __init__(self):
        pass
    
    
    def maximumWealth(self, account):
        """
        Method Name : maximumWealth
        Description : This method help to find the max wealth if all account.
        Output      : maximumWealth in Int
        On Failure  : None
        """
        
        maxWealth = 0      
        for i in range(len(account)):
            totalWealth = sum(account[i])
            if totalWealth > maxWealth:   # Or use max(maxWealth, totalWealth)
                maxWealth = totalWealth 
        return maxWealth

# Driver Code
account = [[1,2,3], [3,2,1]]        
s = Solution()
print(s.maximumWealth(account))