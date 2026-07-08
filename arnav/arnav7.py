lst = ['apple','guava', 'mango', 'banana', 'kiwi']

print("length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('papaya')
print("updated list:", lst)

lst.remove('guava')
print("updated list :", lst)

lst.sort()
print("sorted list :", lst)

lst.pop(1)
print("updated list :", lst)

lst.reverse()
print("reverse list :", lst)

print("Slicing",lst[1:3])