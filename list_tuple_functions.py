print("List & Tuple Functions")
# List | Indexing
# Tuple | No Indexing

# Indices
list_index1 = ['is', 'a', 'This', 'sentence.']
print(list_index1[2], list_index1[0:2], list_index1[3])

# Range Start
list_index2 = ['X', 'Y', 'Start', 'from', 'the', 'end']
print(list_index2[2:])

# Range End
list_index3 = ['Start', 'from', 'the', 'beginning', 'X', 'Y']
print(list_index3[:4])

# Change Index
list_index4 = ['My', 'name', 'is', 'enter_name']
list_index4[3] = "Adrian"

# len()
list_index5 = ['How', 'long', 'is', 'this', 'array?']
print("Length of Array: " + str(len(list_index5)))

# .count()
list_index6 = ['1', '1', '2', '3', '4', '1']
print("1 | Mode: " + str(list_index6.count('1')))

# .insert()
list_index7 = ['Apple', 'Banana', 'Orange']
list_index7.insert(1, 'Carrot')
print(list_index7)

# .remove() | First Occurence is Removed from the Array
list_index7.remove('Apple')
print(list_index7)

# .append() | You Can Append Lists
list_index8 = ['That', 'will', 'be', 'added', 'and', 'removed', '->']
list_index8.append('X')
print(list_index8)

# .pop
removed_index = list_index8.pop()
print(list_index8)

# del/del[]
del list_index8[len(list_index8) - 1] # del index
print(list_index8)
del list_index8 # del list

# clear
list_index9 = ['This', 'will', 'be', 'cleared']
list_index9.clear()
print(list_index9)

# .copy
list_index10 = ['Copy', 'this', 'list']
list_index11 = list_index10.copy()
print(list_index11)

# list++
list_index12 = ['This', 'is']
list_index13 = ['a', 'joint', 'list']
list_index14 = list_index12 + list_index13
print(list_index14)

# .reverse
list_index15 = ['a', 'b', 'c', 'd', 'e']
list_index15.reverse();
print(list_index15)

# .sort
list_index15.sort()
print(list_index15)

# Nested List
list_index16 = [['Boy', 'Ball'], ['Girl', 'Doll']]
print(list_index16[0][1])

# Tuples | Read, Combine, Delete | No Index Access
list_index17 = ('Read', 'Only', 'List')

# Tuples -> List
new_list = list(list_index17) # Must be Stored
print(new_list)

# List -> Tuples
new_tuple = tuple(new_list)
print(new_tuple)