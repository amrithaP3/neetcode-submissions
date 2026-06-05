class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        
        for i in range(9):
            seen = set()
            for x in range(3):
                row = (i // 3) * 3 + x
                for y in range(3):
                    col = (i % 3) * 3 + y
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True