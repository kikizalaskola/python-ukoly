a = int(input("Zadejte A:"))
b = int(input("Zadejte B:"))
c = int(input("Zadejte C:"))
#tipuji ze a je minimum i maximum
min1= a
max1= a
#porovnávám b s mínímem a maximem
if b<min1:
    min1=b
if b>max1:
    max1=b
#porovnávám c s mínímem a maxímem
if c<min1:
    min1=c
if c>max1:
    max1=c

print("Minumum je:", min1)
print("Maximum je:", max1)
