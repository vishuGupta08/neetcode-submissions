
class Solution:

    def canEat(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0

        for bananas in piles:
            # ceil(bananas / k)
            hours += (bananas + k - 1) // k

        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        ans = high

        while low <= high:

            mid = low + (high - low) // 2

            if self.canEat(piles, h, mid):
                ans = mid
                high = mid - 1   # try smaller speed
            else:
                low = mid + 1    # need larger speed

        return ans
        
        