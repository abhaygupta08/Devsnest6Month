class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        i,j =0,len(height)-1
        total = 0
        left=height[i]
        right=height[j]
        while i<j:
            if height[i]>left:
                left=height[i]
            if height[j]>right:
                right=height[j]
            if left<=right:
                total+=left-height[i]
                i+=1
            else:
                total+=right-height[j]
                j-=1
        return total
        