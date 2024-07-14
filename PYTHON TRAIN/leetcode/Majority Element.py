#path: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Réinitialiser le count pour la vérification
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return None