#bitwise operators
a = 10  # Binary: 1010
b = 4   # Binary: 0100

#Manually converting to binary and performing bitwise operations
#here's how the bitwise operations work:
# AND (&): 1010 & 0100 = 0000 (0 in decimal)
# OR (|): 1010 | 0100 = 1110 (14 in decimal)
# XOR (^): 1010 ^ 0100 = 1110 (14 in decimal)  
# NOT (~): ~1010 = ...10101 (-11 in decimal, two's complement representation)
#Shift left (<<): 1010 << 1 = 10100 (20 in decimal)
#Shift right (>>): 1010 >> 1 = 0101 (5 in decimal)



print(a & b)  # Output: 0 (Binary: 0000) & use when both bits are 1
print(a | b)  # Output: 14 (Binary: 1110) | use when at least one bit is 1
print(a ^ b)  # Output: 14 (Binary: 1110) ^ use when bits are different
print(~a)     # Output: -11 (Binary: ...10101) ~ use to invert all bits
print(a << 1) # Output: 20 (Binary: 10100) << use to shift bits left
print(a >> 1) # Output: 5 (Binary: 0101) >> use to shift bits right