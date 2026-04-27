class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {}
        for i in range(len(position)):
            steps = 0
            reach = position[i]
            steps = 1
            while reach <= target:
                reach += speed[i]
                steps +=1
            
            mp[steps] = mp.get(steps,0) +1
        return len(mp)

        