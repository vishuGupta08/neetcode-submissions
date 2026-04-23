class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mp = {}
        window = {}
        res = [-1,-1]
        resLen = float("inf")
        for el in t:
            mp[el] = mp.get(el,0)+1
        have, need = 0, len(mp)
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in mp and window[c] == mp[c]:
                have +=1
            
            # shrinking
            while have == need:
                if right - left +1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in mp and window[s[left]] < mp[s[left]]:
                    have -=1
                
                left +=1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""






        
        
        
        