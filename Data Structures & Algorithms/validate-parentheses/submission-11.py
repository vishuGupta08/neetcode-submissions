class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mp:
                # closing bracket
                if not stack or stack[-1] != mp[ch]:
                    return False
                stack.pop()
            else:
                # opening bracket
                stack.append(ch)

        return len(stack) == 0