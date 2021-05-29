class Solution:
    def solve(self, s0, s1):
        if len(s0)!=len(s1):
            return False
        if s0==s1:
            return True
        s1 = s1+s1
        try:
            if s1.index(s0):
                return True
        except:
            return False