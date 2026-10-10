# **Count how many even and odd numbers** are present in a list.

arr = [4,56,75,67,45,76,5,57,]
evenc = 0
oddc = 0 
for i in range(len(arr)):
    if(arr[i]%2 == 0):
        evenc = evenc + 1
    else:
        oddc = oddc + 1
print("odd count is",oddc)
print("even count is", evenc)
