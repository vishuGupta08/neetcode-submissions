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
                    else:
                        return False
                else:
                    stack.append(el)
            elif el in mp:
                stack.append(el)
        
        if len(stack) == 0:
            return True
        return False

        