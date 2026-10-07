#  **Reverse a list** without using `reverse()` or slicing.

arr = [32,43,34,23,67,89,85,64,74,37]
revers= []
n = len(arr)
for i in range (n):
    revers.append(arr[n-i-1])
print(revers)