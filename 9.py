num=int(input("Enter the two digit number:"))
temp=num
s=0
while temp>0:
    r=temp%10
    s=s*10+r
    temp=temp//10

print(s)