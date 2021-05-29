s = "abbaca"
solution,dup = '',0
stackArr = []
if not s:
    print('EMPTY')
stackArr.append(s[0])
# print(stackArr[-1])
for i in range(1,len(s)):
    print(s[i])
    if len(stackArr)==0:
        stackArr.append(s[i])
    elif stackArr[-1]==s[i]:
        stackArr.pop()
    elif stackArr[-1]!=s[i]:
        stackArr.append(s[i])
for let in stackArr:
    solution += let
print(solution)