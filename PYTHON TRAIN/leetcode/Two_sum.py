class Solution(object):
    def twoSum(self,nums,target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums,target))

nums1 = [3,2,4]
target1 = 6
print(solution.twoSum(nums1,target1))

nums2 = [3,3]
target2 = 6
print(solution.twoSum(nums2,target2))

nums3 = [3,2,3]
target3 = 6
print(solution.twoSum(nums3,target3))