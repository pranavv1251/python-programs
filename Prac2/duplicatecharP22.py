print("Enter the string:")
s=input()
list1=[]
list2=[]
for i in s:
    if i not in list1:
        list1.append(i)
    else:
        list2.append(i)
print("The characters are: ",list1)
print("The duplicate characters are: ",list2)
