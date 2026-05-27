class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # utilize BFS since rotting in 4-directional manner!!
        q = collections.deque()
        
        # count for fresh oranges
        fresh = 0
        time = 0

        # 0 = empty, 1 = fresh, 2 = rotten

        # row by row
        for r in range(len(grid)):
            # col by col
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        # different directions to traverse
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            length = len(q)
            # need this for loop to ensure that during each iteration 
            # of the while loop, all the oranges that were rotten at 
            # the start of that minute are processed simultaneously
            # ensures CORRECT timing!!
            for i in range(length):
                r, c = q.popleft()
                for d in directions:
                    newRow = r + d[0]
                    newCol = c + d[1]
                    # bounds checking!
                    if (newRow < 0 or newRow == len(grid)) or (newCol < 0 or newCol == len(grid[0])) or grid[newRow][newCol]!= 1:
                        continue
                    grid[newRow][newCol] = 2
                    fresh -= 1
                    q.append([newRow, newCol])
            time += 1
        
        # some oranges that we can't make rotten --> fresh != 0
        return time if fresh == 0 else -1
        


