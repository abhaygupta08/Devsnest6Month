class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxi = 0,0,0
        tempChar = {}
        if k==0:
            if s == '':
                return s
            while(r<len(s)):
                if s[r]
        repeat = 0
        
        while(r<len(s)):
            if s[r] not in tempChar:
                tempChar[s[r]] = 1
            else:
                tempChar[s[r]] +=1
            repeat = max(repeat,max(tempChar.values()))
            if r-l+1-repeat > k:
                tempChar[s[l]] -=1
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1
        return maxi
