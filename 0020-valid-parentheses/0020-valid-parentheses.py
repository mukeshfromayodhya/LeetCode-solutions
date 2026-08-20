class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {
                "]": "[",
                "}": "{",
                ")": "("
        }
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if  paranthesis[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        return not stack
