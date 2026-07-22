class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count="0"
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
               count=max(count,num[i:i+3])
        return "" if count=="0" else count
