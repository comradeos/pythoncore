# import collections
# print(collections.Counter(input('Введіть грьобаний тєкст: ')).most_common())

word = "aaab"
d = {}

for i in word:
    d[i] = 1 if i not in d.keys() else d[i]+1
    
print(d)