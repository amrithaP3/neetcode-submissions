class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Push BEFORE rotating
        for i in range(len(boxGrid)):
            row = "".join(boxGrid[i])
            sections = row.split("*")
            pushed = []

            for s in sections:
                stones = s.count("#")
                empties = len(s) - stones

                pushed.append("." * empties + "#" * stones)
            
            boxGrid[i] = list("*".join(pushed))

        # Rotate
        rotatedGrid = [list(row) for row in zip(*boxGrid[::-1])]

        return rotatedGrid
