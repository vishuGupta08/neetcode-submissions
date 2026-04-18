class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, el in enumerate(nums):
            if target-el in mp:
                return [mp[target-el],index]
            mp[el] = index



        