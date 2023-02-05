#2. get the occurence of all vowels and consonent from the large given string.

#define all vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']

str = input("Enter a string: ")

#counter variables
vow = 0 
cons = 0

for i in str:
    
    if i in vowels:
        vow += 1
    elif i != ' ':
        cons += 1

print("Vowels: ", vow)
print("Consonants: ", cons)