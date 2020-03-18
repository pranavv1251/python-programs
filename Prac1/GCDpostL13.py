def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print("Enter two numbers:")
a= int(input()) 
b= int (input())
GCD=gcd(a,b)
print("GCD: ",GCD)