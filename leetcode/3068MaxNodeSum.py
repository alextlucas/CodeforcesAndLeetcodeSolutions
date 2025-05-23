from typing import List
import functools
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        @cache
        def maxSumOfNodes(idx, isEven):
            if idx == len(nums):
                return 0 if isEven == 1 else -float("inf")
            noXorDone = nums[idx] + maxSumOfNodes(idx + 1, isEven)

            xorDone = (nums[idx] ^ k) + maxSumOfNodes(idx + 1, isEven ^ 1)

            return max(xorDone, noXorDone)
            
        
        return maxSumOfNodes(0, 1)
