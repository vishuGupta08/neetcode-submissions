class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for el in nums:
            mp[el] = mp.get(el,0)+1

        arr = []
        buckets = [[] for _ in range(len(nums)+1)]
        count =0
        for num, count in mp.items():
            buckets[count].append(num)
        for i in range(len(buckets)-1,-1,-1 ):
            for el in buckets[i]:
                arr.append(el)
                if(len(arr)>k-1):
                    return arr
        