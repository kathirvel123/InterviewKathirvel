#Top k frequent elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        h=[]
        d=sorted(d,key=lambda x:d[x],reverse=True)
        return d[:k]