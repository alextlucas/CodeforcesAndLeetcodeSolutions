from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #starting with 0
        res1 = []
        cur = 0
        for i in range(len(words)):
            if cur == 0 and groups[i] == 0:
                res1.append(words[i])
                cur = 1
            elif cur == 1 and groups[i] == 1:
                res1.append(words[i])
                cur = 0
        #starting with 1
        res2 = []
        cur = 1
        for i in range(len(words)):
            if cur == 1 and groups[i] == 1:
                res2.append(words[i])
                cur = 0
            elif cur == 0 and groups[i] == 0:
                res2.append(words[i])
                cur = 1
        
        return res1 if len(res1) > len(res2) else res2


