
from re import M


class Solution:
    def __init__(self):
        pass
        
    def mostWordsFound(self, sentence):
        """
        Method Name : mostWordsFound
        Description : This method help to find the how many words in the sentence.
        OutPut      : Int
        On Failure  : None
        """
        return max(len(i.split())  for i in sentence)
        
#  Driver Code
sentence = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
s = Solution()
print(s.mostWordsFound(sentence))
        
