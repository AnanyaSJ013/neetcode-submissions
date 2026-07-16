class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            cursum=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]<=nums[j-1]:
                    break
                cursum+=nums[j]
            sum=max(sum,cursum)
        return sum
