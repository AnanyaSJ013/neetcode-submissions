class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=""
        i=j=0
        while i < len(word1) and j < len(word2):
            l+=word1[i]+word2[j]
            i=i+1
            j=j+1
        if len(word1)>len(word2):
            l+=word1[j:]
        else:
            l+=word2[i:]
        return l