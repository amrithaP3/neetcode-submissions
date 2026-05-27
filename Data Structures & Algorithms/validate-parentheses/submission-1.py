class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"(": ")", "[": "]", "{":"}"}

        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            elif stack:
                openBracket = stack.pop()
                if s[i] != pairs[openBracket]:
                    return False
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
            
                