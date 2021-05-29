class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        if len(nums)%2:
            middleInd = int(len(nums)/2)
            return float(nums[middleInd])
        else:
            middleInd1 = int(len(nums)/2) - 1
            middleInd2 = middleInd1+1
            return float((nums[middleInd1]+nums[middleInd2])/2)