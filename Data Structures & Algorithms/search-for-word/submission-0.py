class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # make sure you don't revisit same position twice!! 
        path = set()

        def dfs(r, c, i):
            # base cases...
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            # removing position from path to make it empty to try the next word chain
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                # checks different start positions in board until
                # start position with word chain found!
                if dfs(r, c, 0):
                    return True
        
        return False
