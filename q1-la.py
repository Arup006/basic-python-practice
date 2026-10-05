# */ **Find the sum of all numbers in a list** without using `sum()`.

list0=[34,45,65,36,67,37,48,26,52]
length=len(list0)
sumation = 0

for i in range(length):
 sumation = sumation + list0[i]
print(sumation)