class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(o, c):
            # base case to add combo into res
            if o == c == n:
                res.append("".join(stack))
                return
            
            # 2 possible decisions...

            # decision 1: add (
            if o < n:
                stack.append("(")
                backtrack(o + 1, c)
                stack.pop()
            
            # decision 2: add )
            if o > c:
                stack.append(")")
                backtrack(o, c + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
