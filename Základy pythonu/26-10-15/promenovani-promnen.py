a = int(input("Zadejte A:"))
b = int(input("Zadejte B:"))
c = int(input("Zadejte C:"))
temp = 0

if a > b:
    temp = a
    a = b
    b = temp

if b>c:
    temp = b
    b =c
    c=temp

if a>b:
    temp =a
    a=b
    b=temp    

print(a, b, c)