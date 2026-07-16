class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=sorted(heights)
        sum=0
        for i in range(len(heights)):
            if(heights[i]!=s[i]):
                sum+=1
        return sum