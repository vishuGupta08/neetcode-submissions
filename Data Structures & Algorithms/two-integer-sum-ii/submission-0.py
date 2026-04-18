class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = set()
        for index, num in enumerate(numbers):
            if target - num in st:
                return [min(index+1, numbers.index(target-num)+1), max(index+1, numbers.index(target-num) +1)]
            else: 
                st.add(num)              
        