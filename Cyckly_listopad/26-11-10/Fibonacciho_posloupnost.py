doba_simulace = int(input("Zadejte počet měsíců na simulaci: "))
mesice = 1
#dospeli¨
a = 0
#mladata 
b= 1
#pomocna promena
dopredu = a+b

print("-" * 20)
print(f"Měsíc {mesice}: {dopredu} pár(ů) ", "🐁"*dopredu)
while mesice<doba_simulace:
    mesice +=1
    dopredu = a + b
    a = b
    b = dopredu
    print("-" * 20)
    print(f"Měsíc {mesice}: {dopredu} pár(ů) ", "🐁"*dopredu)
