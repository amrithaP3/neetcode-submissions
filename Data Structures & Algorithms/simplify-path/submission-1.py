class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [item for item in path.split("/") if item]
        stack = []

        for p in paths:
            if p == ".":
                continue
            
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/" + p)
        
        if not stack:
            return "/"
        else:
            return "".join(stack)