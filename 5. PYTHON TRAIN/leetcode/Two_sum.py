class Solution(object):
    def twosum(self,nums,target):
        nums_idice = {}
        
        for i, num in enumerate(nums):
            nums_idice[num] = i
            
        nums = sorted(nums)
        # print(nums)
        # We start on the first element of the list
        left = 0
        # we start of the end of our list 
        right = len(nums) -1 
        
        while left < right: 
            sum = nums[left] + nums[right]
            
            # Si la sum des 2 nombre dans list et égale a notre target
            # Alors 
            if sum == target : 
                index1 = nums_idice[nums[left]]
                index2 = nums_idice[nums[right]]
                # print(index1, index2)
                if index1 == index2:
                    index1 -=1
                return [index1,index2]
                
            
            elif sum < target:
                left = left + 1
            else: 
                right= right -1
            
      
        

solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twosum(nums,target))

nums1 = [3,2,4]
target = 6
print(solution.twosum(nums1,target))

nums2 = [3,3]
target = 6
print(solution.twosum(nums2,target))
