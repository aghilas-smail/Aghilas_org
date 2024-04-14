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


#Avec une boucle 

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
    
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True


# print(is_palindrome("ababa"))  
# print(is_palindrome("abb"))    
# print(is_palindrome("baabb"))  
