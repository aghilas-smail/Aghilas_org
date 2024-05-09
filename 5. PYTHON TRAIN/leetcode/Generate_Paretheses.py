# link : https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left,right,s):
            # verify if the len of s  = s*2
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1,right,s + '(')
            
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0,0,'')
        return res

solution = Solution()
print(solution.generateParenthesis(3))  
print(solution.generateParenthesis(1)) 
print(solution.generateParenthesis(5))  