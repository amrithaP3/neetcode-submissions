class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                x = i + 1
                y = len(nums) - 1
                
                while (x < y):
                    potentialSum = nums[i] + nums[x] + nums[y]
                    if potentialSum > 0 :
                        y -= 1
                    elif potentialSum < 0:
                        x += 1
                    else:
                        triplet = [nums[i], nums[x], nums[y]]
                        res.append(triplet)

                        # IMPORTANT bc still want to check for more triplets
                        # while x < y!! LOOK at example they give you
                        x += 1
                        while (nums[x] == nums[x - 1] and x < y):
                            x += 1
        return res
