class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # time complexity: O(n)
        # make sure length of s1 fits within s2
        if len(s1) > len(s2):
            return False
        
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1
        
        if s1count == s2count:
            return True

        l = 0
        for i in range(len(s1), len(s2)):
            if l > len(s2) - len(s1):
                break
            
            s2count[ord(s2[l]) - ord("a")] -= 1
            s2count[ord(s2[i]) - ord("a")] += 1
            l += 1
    
            if s1count == s2count:
                return True

        return False

        # time complexity: O(n * m)
        '''
        # make sure length of s1 fits within s2
        if len(s1) > len(s2):
            return False
        
        s1count = defaultdict(lambda: 0)
        s2count = defaultdict(lambda: 0)

        for i in range(len(s1)):
            s1count[s1[i]] += 1
        
        counter = len(s1)
        i = 0
        start = i
        while i < (len(s2)) and start < (len(s2) - len(s1) + 1):
            s2count[s2[i]] += 1
            counter -= 1
            i += 1

            if counter == 0:
                if s1count == s2count:
                    return True
                s2count = defaultdict(lambda: 0)
                counter = len(s1)
                start += 1
                i = start
        
        return False
        '''


