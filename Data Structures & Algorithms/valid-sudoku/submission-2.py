class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. CHECK ALL ROWS
        # Iterate over each row
        for i in range(9):
            seen = set()

            # Iterate over each column
            for x in range(9):
                if board[i][x] == ".":
                    continue

                if board[i][x] in seen:
                    return False
                else:
                    seen.add(board[i][x])
        
        # 2. CHECK ALL COLUMNS
        # Iterate over each column
        for i in range(9):
            seen = set()

            # Iterate over each row
            for x in range(9):
                if board[x][i] == ".":
                    continue

                if board[x][i] in seen:
                    return False
                else:
                    seen.add(board[x][i])
        
        # 3. CHECK ALL 3x3 BOXES (9 such NON-OVERLAPPING boxes)
        # Iterate over each 3x3 box
        for i in range(9):
            seen = set()

            # Iterate over each row
            for x in range(3):
                row = (i // 3) * 3 + x
                # Iterate over each column
                for y in range(3):
                    col = (i % 3) * 3 + y

                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True
