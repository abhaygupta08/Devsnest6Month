class Solution:
    def solve(self, n):
        s = []
        while n % 2 == 0:
            s.append(2)
            n = n // 2
        for i in range(3,int(n**0.5)+1,2):
            while n % i== 0:
                s.append(i)
                n = n // i
        if n > 2:
            s.append(n)
        return s