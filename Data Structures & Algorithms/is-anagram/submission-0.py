class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        mp = {}
        for el in s:
            mp[el] = mp.get(el,0) +1

        for el in t:
            mp[el] = mp.get(el,0)-1

        for el in mp:
            if mp[el]>0:
                return False
        return True
        