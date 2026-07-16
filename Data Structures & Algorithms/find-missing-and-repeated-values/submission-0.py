class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
       n=len(grid)
       d=m=0
       for num in range(1,n*n+1):
        c=0
        for i in range(n):
            for j in range(n):
                if num==grid[i][j]:
                    c+=1
        if c==2:
            d=num
        elif c==0:
            m=num
       return [d,m]
