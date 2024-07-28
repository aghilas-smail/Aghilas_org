#link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        
        i = 1
        count = 1

        for j in range(1,len(nums)):
            if nums[j] == nums[j - 1]:
                count = count + 1
            else : 
                count = 1
            
            if count <= 2:
                nums[i] = nums[j]
                i += 1
        return i 