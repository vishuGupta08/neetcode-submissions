class Solution:

    def encode(self, strs: List[str]) -> str:
        output= ''
        for el in strs:
            output = output + el + 'è'
        return output

    def decode(self, s: str) -> List[str]:
        s = s.split('è')
        s.pop()
        return s
