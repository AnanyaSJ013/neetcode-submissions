class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count={}
      for i in nums:
        count[i]=count.get(i,0)+1
      count=sorted(count.items(),key=lambda item:item[1],reverse=True)
      return[i[0] for i in count[:k]]