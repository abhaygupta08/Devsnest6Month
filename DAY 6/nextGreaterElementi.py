class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        solution = []
        maxi = None
        for i in range(len(nums1)):
            indexInnums2 = nums2.index(nums1[i])
            if indexInnums2 == len(nums2)-1:
                solution.append(-1)
            else:
                for j in range(indexInnums2+1,len(nums2)):
                    if nums2[j]>nums1[i]:
                        maxi = nums2[j]
                        break
                    else:
                        maxi = -1
                solution.append(maxi)
        return solution