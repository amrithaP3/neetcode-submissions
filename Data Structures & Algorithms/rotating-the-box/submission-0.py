class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        # Update the box to reflect felled stones
        for i in range(len(boxGrid)):
            # define sections based on where obstacles are
            row = "".join(boxGrid[i])
            sections = row.split("*")
            pushed = []

            for section in sections:
                stones = section.count("#")
                empties = len(section) - stones

                pushed.append("." * empties + "#" * stones)
            
            boxGrid[i] = list("*".join(pushed))
        
        # Rotate boxGrid clockwise
        rotatedGrid = [list(row) for row in zip(*boxGrid[::-1])]

        return rotatedGrid
