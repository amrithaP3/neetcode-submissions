class Solution:
    # better to do with dicts in terms of efficiency?
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        # This is the list version O(n logn)
        if len(s) != len(t):
            return False
        a = []
        b = []
        for i in range(len(s)):
            a.append(s[i])
            b.append(t[i])
        
        a.sort()
        b.sort()

        if a == b:
            return True
        else:
            return False
        '''

        # This is the dictionary version - O(n)
        if len(s) != len(t):
            return False
        
        a, b = {}, {}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] += 1
            else:
               a[s[i]] = 1 
            if t[i] in b:
                b[t[i]] += 1
            else:
               b[t[i]] = 1
        
        if a == b:
            return True
        else:
            return False