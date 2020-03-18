print("Enter the string:")
s=input()
list2=[]
list1=[',','?','!',':',';','.']
for i in s:
    if i not in list1:
        list2.append(i)
c=" "
for a in list2:
    c+=a
print(c)
    