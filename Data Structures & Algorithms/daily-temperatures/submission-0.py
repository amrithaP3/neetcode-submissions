class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Ensures that the necessary result indices remain 0
        res = [0] * len(temperatures)

        # Monotonic decreasing order stack
        stack = []  # (index, temp)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index = stack.pop()[0]
                res[index] = i - index
            # push to stack if colder temp or when 
            # even colder temps have been popped
            stack.append((i, t))
        
        return res