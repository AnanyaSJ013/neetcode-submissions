class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
       s=Counter(nums)
       nums.sort(key=lambda n: (s[n], -n))
       return nums
