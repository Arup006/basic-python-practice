# **Find the smallest element in a list** without using `min()`.

list1 = [35,45,53,75,65,4,53,20,51,42,64,86]
small = list1[0]
n = len(list1)
for i in range (n):
    if (list1[i] < small):
        small=list1[i]
print(small)

