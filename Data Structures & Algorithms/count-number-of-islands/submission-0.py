class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(newRow, newCol, visited):
            q = collections.deque()
            visited.add((newRow, newCol))
            q.append((newRow, newCol))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                row, col = q.popleft()

                for d in directions:
                    r, c = row + d[0], col + d[1]

                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    bfs(row, col, visited)
        
        return islands