class Solution:
    def solve(self, s):
        if len(s)==0 or len(s)==1:
            return -1
        res = False
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                res = True
        if res:
            return 2
        r = False
        for i in range(2,len(s)):
            if s[i]==s[i-2]:
                r = True
        if r:
            return 3
        return -1
        