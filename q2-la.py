# **Find the largest element in a list** without using `max()`.

list1 = [34,54,64,32,57,85,14,36,47]
lrg=0
for i in range(len(list1)):
    if(list1[i] > lrg):
        lrg = list1[i]
print(lrg)    
