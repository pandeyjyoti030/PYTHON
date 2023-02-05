#6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.


list1 = [1, 3, 5, 7, 9, 11, 13]
list2 = [2, 4, 6, 8, 10, 12, 14]
list3 = list()

odd = list1[1::2]
print("Element at odd-index positions from list one")
print(odd)

even = list2[0::2]
print("Element at even-index positions from list two")
print(even)

print("Printing Final third list")
list3.extend(odd)
list3.extend(even)
print(list3)