doba_simulace = int(input("Zadejte počet měsíců na simulaci: "))
mesice = 1
#dospeli¨
a = 0
#mladata 
b= 1
#pomocna promena
par = a+b

print("-" * 20)
print(f"Měsíc {mesice}: {par} pár(ů) ", "🐁"*par)
while mesice<doba_simulace:
    mesice +=1
    par = a + b
    a = b
    b = par
    print("-" * 20)
    print(f"Měsíc {mesice}: {par} pár(ů) ", "🐁"*par)
