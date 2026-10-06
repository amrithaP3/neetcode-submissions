class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Approach: Go in one direction until you need to turn right
            * next cell = out of bounds
            * next cell = visited
        '''
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        totalElements = rows * cols
        visited = set()

        # directions in turn order
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        current = (0,0)

        while len(visited) != totalElements:
            visited.add(current)
            res.append(matrix[current[0]][current[1]])

            # Check if it's time to turn right!
            # Get next cell when moving in current direction
            nr, nc = (current[0] + directions[d][0], current[1] + directions[d][1])

            if not 0 <= nr < rows or not 0 <= nc < cols or (nr, nc) in visited:
                d = (d + 1) % 4
            
            current = (current[0] + directions[d][0], current[1] + directions[d][1])

        return res
            

                


