n1 = [1,2,3,5,6,8,9]

val = 9
mid = len(n1)//2

st = 0
end = len(n1)
while n1[mid]!=val:
    mid = (end + st)//2
    if n1[mid]==val:
        print(n1[mid])
        print("FOund")
        break
    if val < n1[mid]:
        print(n1[mid],n1[st:end])
        end = mid+1
    else:
        print(n1[mid],n1[st:end])
        st = mid+1
print("NF")