class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals in chronological order
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals:
            prev_start = res[-1][0]
            prev_end = res[-1][1]

            if start <= prev_end:
                if end > prev_end:
                    res[-1] = [prev_start, end]
            else:
                res.append([start, end])
        
        return res


