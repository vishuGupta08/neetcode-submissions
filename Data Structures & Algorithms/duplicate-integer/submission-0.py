class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for el in nums:
            mp[el] = mp.get(el,0)+1
            if(mp[el]>1):
                return True
        return False

        