from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        changes = [0] * len(nums)

        for l,r in queries:
            #subtract in the front and add in the back
            changes[l] -= 1
            if r + 1 < len(nums):
                changes[r + 1] += 1
        
        running = 0
        for i in range(len(nums)):
            running += changes[i]
            if nums[i] + running > 0:
                return False
        
        return True

