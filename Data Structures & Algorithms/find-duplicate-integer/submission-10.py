class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can't sort and need ot use O(1) space so can't use hashset
        
        # linked list problem and use floyd's ag.

        # value in each index is like a pointer in a linked list
        ## the value points to that index since everything in the
        ## the range [1, n] which also guarantees that index 0
        ## never a part of the cycle because it's outside the range
        # so find a cycle in a linked list using floyd's alg.

        slow, fast = 0, 0

        # find intersection point that proves existence of cycle
        # with fast and slow pointers

        # while True to keep going until intersection point found
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow



