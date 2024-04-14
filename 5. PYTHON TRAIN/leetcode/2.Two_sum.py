class Solution(object):
    def twosum(self,nums,target):
        nums_idice = {}
        
        for i, num in enumerate(nums):
            nums_idice[num] = i
            
        nums.sort()
        
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
                return [index1,index2]
            
            elif sum < target:
                left = left + 1
            else: 
                right= right -1