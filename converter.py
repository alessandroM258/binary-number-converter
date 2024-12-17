def decimalToBinary(num):
    binary_string = bin(num)[2:]
    print(binary_string)
theSandwich = int(input("enter binary number and convert it to a decimal"))
if theSandwich >= 0:
    decimalToBinary(theSandwich)
else:
    print("you don't get a The Sandwich")