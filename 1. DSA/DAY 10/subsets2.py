class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                l=len(res)
            for j in range(len(res)-l,len(res)):
                res.append(res[j]+[nums[i]])
        return res