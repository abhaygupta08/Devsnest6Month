strs = ["eat","tea","tan","ate","nat","bat"]
tempStrsSorted = {}
solution = []
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
for strg in strs:
    newstrg = ''
    for temp in sorted(strg):
        newstrg += temp
    if not newstrg in tempStrsSorted:
        tempStrsSorted[newstrg] = []
    tempStrsSorted[newstrg].append(strg)
for tempSorted in tempStrsSorted:
    solution.append(tempStrsSorted[tempSorted])
print(solution)


# tempStrsSorted = {
#     'test':['aa','bb','cc']
# }
# print(tempStrsSorted['test'][1])