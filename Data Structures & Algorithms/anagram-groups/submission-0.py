class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for el in strs:
            key = "".join(sorted(el))
            if key not in mp:
                mp[key] = []
            mp[key].append(el)
        output = []
        for el in mp:
            output.append(mp[el])
        return output
        