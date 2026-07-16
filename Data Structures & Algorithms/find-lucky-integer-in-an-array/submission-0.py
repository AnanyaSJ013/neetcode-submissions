class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f=Counter(arr)
        res=-1
        for key,value in f.items():
            if key==value:
                res=max(res,key)
        return res