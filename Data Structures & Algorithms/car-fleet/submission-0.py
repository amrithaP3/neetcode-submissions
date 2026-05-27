class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # Important to sort position by DEC. order
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for p, s in cars:
            hours = (target - p) / s
            stack.append(hours)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
