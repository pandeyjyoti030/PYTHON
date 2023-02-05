#4. Reverse the list by using negative index and apply logic also.

#negative indexing

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list1[::-1])

#using logic

list2 = ['apple', 'banana', 'cherry', 'mango']
reversedList = []
 
#reverse list using for loop
for i in range(len(list2)) :
    reversedList.append(list2[len(list2) - i - 1])
 
print(reversedList)

