class Solution(object):
    def isValid(self, s):
        opened = "{(["
        closed = "})]"
        mapping = []
        for char in s :
            if char in opened:
                mapping.append(char)
            elif char in closed:
                if not mapping:
                    return False
                if opened.index(mapping.pop()) != closed.index(char):
                    return False
        return not mapping

solution = Solution()
input_string = "()"
print(solution.isValid(input_string))

#link : https://leetcode.com/problems/valid-parentheses/
