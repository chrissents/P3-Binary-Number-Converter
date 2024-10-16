# Extra Credit Code (Beyond 15)
def decimalToBinary(num):
    binary_str = bin(num)[2:]
    print(binary_str)

# How the code translates the binary to decimal
def decimalToBinary(num):
    binary_str = bin(num)[2:]
    binary_str = binary_str.zfill(4)
    print(binary_str)

# How it prints out the finished product
decimalToBinary(9)
decimalToBinary(0)
decimalToBinary(15) 

# Extra Credit Portion (Beyond 15)
decimalToBinary(69)
decimalToBinary(20) 
decimalToBinary(105) 