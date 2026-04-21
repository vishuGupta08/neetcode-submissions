import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        # quick sort
        def quickSelect(left, right):
            pivot = nums[random.randint(left,right)]

            l,r = left, right

            while l <=r :
                while nums[l] < pivot:
                    l +=1
                while nums[r] > pivot:
                    r -=1
                
                # need swapping
                if l<=r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l +=1
                    r -=1
            
            if k <=r:
               return quickSelect(left,r)
            elif k >=l:
              return  quickSelect(l, right)
            else:
                return nums[k]

        return quickSelect(0, len(nums)-1)
                 
        