
class Solution:
    def __init__(self):
        pass
    
    def restoreString(self, s, indices):
        """
        Method Name     :  restoreString
        Description     : In this method we are restoring the string using indices.
        OutPut          : string
        On Failure      : None
        """
        
        res = [''] 
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(i for i in res)
    
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s = Solution()
print(s.restoreString(s, indices))