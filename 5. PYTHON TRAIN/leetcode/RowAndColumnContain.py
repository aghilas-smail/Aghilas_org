"""Check if Every Row and Column Contains All Numbers
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.



Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3. 
Hence, we return true.
"""


def Solution(matrix: list[list[int]]) -> bool:
    
    n = len(matrix)
    n2 = set(range(1, n + 1))
    
    for i in range(n): 
        
        row = set(matrix[i])
        col = set(matrix[i][j] for j in range(n))
        
        if set(row) != n2:
            return False
        if set(col) != n2:
            return False
        
    return True


matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
print(Solution(matrix))  