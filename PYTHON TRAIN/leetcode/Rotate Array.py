# link: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(n)
        k = k % n # We use it to normalize k
        print(k)
        
        nums.reverse()
        print(nums)
        nums[:k] = reversed(nums[:k])
        print(nums[:k])
        nums[k:] = reversed(nums[k:])
        print(nums[k:])


solution = Solution()        
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 106 # number of retation 
solution.rotate(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]