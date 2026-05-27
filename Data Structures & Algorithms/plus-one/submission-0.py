class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = ""
        for i in range(len(digits)):
            start += str(digits[i])
        
        num = int(start)
        num += 1

        num = str(num)

        res = []
        for i in range(len(num)):
            res.append(int(num[i]))
        
        return res