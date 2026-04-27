class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '{', '[']
        closeBrackets = [')', '}', ']']
        mp = {
            '(':')',
            '[':']',
            '{':'}'
        }
        if(len(s) <2):
            return False
        stack = []
        for el in s:
            if len(stack) > 0:
                if el not in openBrackets:
                    if len(stack)> 0 and el == mp[stack[-1]]:
                        stack.pop()
                        if el == s[len(s)-1]:
                            return True
                    else:
                        return False
                else:
                    stack.append(el)
            elif el in mp:
                stack.append(el)
            else:
                return False
        if len(stack) > 0:
            return False

        