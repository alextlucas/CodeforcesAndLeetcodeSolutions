from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (check(words[i], words[j]) and dp[j] + 1 > dp[i] 
                    and groups[i] != groups[j]):
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        res = []
        i = max_index
        while i >= 0:
            res.append(words[i])
            i = prev[i]
        res.reverse()
        return res

        
            





        
