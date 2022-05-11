dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
newDict = {}
for key, val in dict.items():
    if val >= 3:
        newDict[key] = dict[key]
print(newDict)