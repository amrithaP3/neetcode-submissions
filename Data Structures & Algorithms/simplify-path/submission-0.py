class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [item for item in path.split("/") if item]
        stack = []

        for path in paths:
            if path == ".":
                continue
            
            if path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/" + path)
        
        if not stack:
            return "/"
        else:
            return "".join(stack)