class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Rearrange horizontally - bottom row moved to the top
        matrix.reverse()

        # Transpose matrix - make rows into columns
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
               temp = matrix[i][j]
               matrix[i][j] = matrix[j][i]
               matrix[j][i] = temp