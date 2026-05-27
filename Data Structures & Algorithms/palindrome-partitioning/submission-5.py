class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # time complexity = O(n * 2^n)
        res = []
        
        def dfs(i, partition, j):
            # reached end of string so current partition = VALID
            if i >= len(s):
                res.append(partition.copy())
                return
            if j >= len(s):
                return
            # exploring all end positions j for a substr starting at i
            # for j in range(i, len(s)):
            #     if self.isPalindrome(s, i, j):
            #         # add current valid substr to path
            #         partition.append(s[i: j + 1])
            #         # recursively call dfs for the rest of the string
            #         dfs(j + 1, partition)
            #         # backtrack by removing the last added substring
            #         partition.pop()

            # Option 1: Try current substring s[i:j+1] if palindrome
            if self.isPalindrome(s, i, j):
                partition.append(s[i:j+1])
                dfs(j + 1, partition, j + 1)  # Move to next i = j+1
                partition.pop()

            # Option 2: Skip extending substring now, try extending further
            dfs(i, partition, j + 1)
            
        dfs(0, [], 0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
