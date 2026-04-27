class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '{', '[']
        closeBrackets = [')', '}', ']']
        mp = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []
        for el in s:
            
            if len(stack) > 0:
                if el not in mp:
                    if el == mp[stack[-1]]:
                        stack.pop()
                        if(len(stack) == 0):
                            return True
                    else:
                        return False
                else:
                    stack.append(el)
            else:
                stack.append(el)
        

        