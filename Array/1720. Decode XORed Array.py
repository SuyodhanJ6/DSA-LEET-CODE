from base64 import encode


class Solution:
    def __init__(self):
        pass
    
    def decode(self, encoded, first):
        
        """
        Method Name  : decode
        Description  : This method find the real or hidden array using another array.
        Output       : array
        On Failure   : None
        """
        ## res  = [1]
        res = [first]
        for i in encoded:
            res.append(res[-1] ^ i)
        return res
    
encoded = [1,2,3]
first = 1
s = Solution()
print(s.decode(encoded, first))