Given numbers from `1` to `n` with one number missing, **find the missing number**.
numbers = [1,2,3,4,5,6,7,8,10,26]

MissingNumber = []
lenth = 27
for i in range (lenth):
    if i not in numbers:
        MissingNumber.append(i)
print(MissingNumber)

