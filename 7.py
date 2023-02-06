
# 7. Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by using list comprehension 
# dict ={"key1":1234, "k2":"ram"}
# list= [1234,"ram"]


dict = {"key1":1234, "k2":"ram"}
list = [1234,'ram']

print("Given dictionary:",dict)
print("Given list:",list)

update = any(item in dict for item in list) 
print (list)