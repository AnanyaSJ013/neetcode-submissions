class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        res=[]
        for num in nums1:
            ng=-1
            for i in range(n-1,-1,-1):
                if nums2[i]>num:
                    ng=nums2[i]
                elif nums2[i]==num:
                    break
            res.append(ng)
        return res