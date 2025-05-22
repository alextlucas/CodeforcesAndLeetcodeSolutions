from typing import List
import heap

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x:x[0])
        heap = []
        difference = [0] * (len(nums) + 1)
    
        j = 0
        operations = 0
        for i in range(len(nums)):
            
            operations += difference[i]

            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while operations < nums[i] and heap and -heap[0] >= i:
                operations += 1
                right = -heappop(heap)
                difference[right + 1] -= 1
            if operations < nums[i]:
                return -1

        return len(heap)