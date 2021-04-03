s = 'abca'
'''
APPOACH 1 
BRUTEFORCE


if s==s[::-1]:
    print('True')
    exit()
for i in range(len(s)):
    tempList = []
    for j in range(len(s)):
        if not i == j:
            tempList.append(s[j])
    if tempList==tempList[::-1]:
        print('mil gya palindorme')
        print(tempList)
        exit()
print('nahi ho payega')

'''
## go from both ends to center
## if they are equal pass
## else try removing left chk for palindrome also try removing right and chk it
## if any works then OKk
## return False

TWO POINTER APPROACH
l,r = 0,len(s)-1
if s==s[::-1]:
    print('palindrome')
    exit()

while(l<r+1):
    if s[l]==s[r]:
        l+=1
        r-=1
    else:
        rmleft,rmright = s[l+1:r+1],s[l:r]
        print(rmleft==rmleft[::-1] or rmright==rmright[::-1])
        exit()