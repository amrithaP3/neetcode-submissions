class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Approach: Go in one direction until you need to turn right
            * next cell = out of bounds
            * next cell = visited
        '''
        res = []
        totalElements = len(matrix) * len(matrix[0])
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
            next_cell = (current[0] + directions[d][0], current[1] + directions[d][1])

            # next_cell out of bounds
            if next_cell[0] > (len(matrix) - 1) or next_cell[1] > (len(matrix[0]) - 1) or next_cell[0] < 0 or next_cell[1] < 0:
                d = (d + 1) % 4
            
            # next_cell in visited
            if next_cell in visited:
                d = (d + 1) % 4
            
            current = (current[0] + directions[d][0], current[1] + directions[d][1])

        return res
            

                


