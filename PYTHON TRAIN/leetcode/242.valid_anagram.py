# Have the same caracteres in the both string.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if the key doesn't existe in the hashmap then return 0
            countT[t[i]] = 1 + countT.get(t[i], 0) 
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False # we know that they have different caracters.
        return True

solution = Solution()
s = "aabbf"
t = "aabbf"
print(solution.isAnagram(s,t))