class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"(": ")", "[": "]", "{":"}"}

        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            elif stack and s[i] == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        
        # checks if stack is empty
        if not stack:
            return True
        else:
            return False
            
                