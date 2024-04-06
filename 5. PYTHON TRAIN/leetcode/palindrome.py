# https://leetcode.com/problems/remove-palindromic-subsequences/
class Solution(object):
    def removePalindromeSub(self, s):
        if s is None:
            return 0
        elif s == s[::-1]: # du coup de ::-1 sert a dire si on peut la lire de gauche a droit et l'inverse
            return 1
        else:
            return 2

# test case
solution = Solution()
print(solution.removePalindromeSub("ababa"))
