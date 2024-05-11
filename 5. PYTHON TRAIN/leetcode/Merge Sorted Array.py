# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if m == 0:
#             nums1[:] = nums2[:]
#             return

#         nums1_copy = nums1[:m]


#         p1 = 0
#         p2 = 0
#         p = 0

#         while p1 < m and p2 < n:
#             if nums1_copy[p1] <= nums2[p2]:
#                 nums1[p] = nums1_copy[p1]
#                 p1 += 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 += 1
#             p += 1


#             if p1 < m:
#                 nums1[p:] = nums1_copy[p1:]

            
#             if p2 < n:
#                 nums1[p:] = nums2[p2:]


''' Easy solution'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # empty list to store the merged result
        merged = []
        
        # Pointers 
        p1 = 0
        p2 = 0
        
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        while p1 < m:
            merged.append(nums1[p1])
            p1 = p1 + 1
        while p2 < n:
            merged.append(nums2[p2])
            p2 = p2 + 1
            
        nums1[:m + n] = merged