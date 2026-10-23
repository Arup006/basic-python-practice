Remove duplicates from a list**
list1= [2,2,4,6,45,45,75,884,78,52,52,51,51]
put = []
for i in range (len(list1)):
  if (list1[i] not in put):
    put.append(list1[i])
print (put)


#   for i in range (len(arr)):
#   duplicate = False
  
#   for j in range (len(arr)-i):
#     if (arr[i]==Nandita[j]):
#       duplicate = True
      
#   if (duplicate == False):
#     Nandita.append(arr[i])
    
# print(Nandita)

