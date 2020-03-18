print("Enter the string:")
s = input()
print("Enter the word:")
a = input()
count = 0
list1 = s.split()
for i in list1:
    if(i == a):
        count += 1
print("The occurence of the word is: ", count)
