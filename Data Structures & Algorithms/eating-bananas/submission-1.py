
class Solution:

    def canEat(self,piles: List[int], k:int, h:int) -> bool:
        hours = 0
        for banana in piles:
            hours += (banana + k -1) // k

        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int)-> int:
        low = 1;
        high = max(piles)
        ans = high
        while low <=high:
            mid = low + (high-low)//2

            if self.canEat(piles,mid,h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans
