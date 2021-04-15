'''
def powerxn(num1,num2):
    if num2==1:
        return num1
    return powerxn(num1,num2-1)*num1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return powerxn(1/x,n)
        return powerxn(x,n)
'''

def powerxn(x,n):
    if n==1:
	    return x
    return powerxn(x,n/2)**2
x,n = 2,3


if n%2:
    ans = powerxn(x,n-1)*x
else:
    ans = powerxn(x,n)
print(ans)



'''
CLASS SOLn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        isxneg,isnneg = x<0,n<0
        x,n = abs(x),abs(n)
        if n==0:
            return 1
        if n==1:
            return 1/x if isnneg else x
        pwr =self.myPow(x,n//2)
        ans = pwr*pwr if n%2==0 else pwr*pwr*x
        
        if isxneg and n%2==1:
            ans = -ans
        if isnneg:
            ans = 1/ans
        return ans
'''