#3. convert a number into binary and binary to number.


def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal

print( binaryTodecimal(1010) ) #10
print( binaryTodecimal(1101) ) #13

#decimal to binary

def dectobin(decimal):
    if(decimal > 0):
        dectobin((int)(decimal/2))
        print(decimal%2, end='')
        
decimal = int(input("Enter a decimal number \n"))
dectobin(decimal)
