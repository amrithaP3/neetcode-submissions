class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Apply pushes per row
        for i in range(len(boxGrid)):
            pushed = []
            row = "".join(boxGrid[i])

            # Get sections that stones can fall through
            # Sections separated by *
            sections = row.split("*")
            for s in sections:
                stones = s.count("#")
                empties = len(s) - stones
                
                pushed.append("." * empties + "#" * stones)
            
            boxGrid[i] = list("*".join(pushed))
        
        # Apply rotation
        rotatedGrid = [list(col) for col in zip(*boxGrid[::-1])]

        return rotatedGrid