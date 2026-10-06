class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1. Flip upside down
        matrix.reverse()

        # 2. Transpose
        # Only swap for pairs above diagonal to avoid double-swapping
        # Diagonal elements stay the same!
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # Do steps in opposite order for counter-clockwise rotation