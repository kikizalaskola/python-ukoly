hodina = int(input("Kolik je hodin? "))
if hodina<0:
    print("Hodina nemůže být záporná")
elif hodina>24:
    print("Zadávejte platné hodiny.")
elif hodina <6:
    print("Dobrou noc")
elif hodina <10:
    print("Dobré ráno")
elif hodina <12:
    print("Dobré dopoledne")
elif hodina ==12:
    print("Dobré poledne")
elif hodina <17:
    print("Dobré odpoledne")
elif hodina <22:
    print("Dobrý večer")
elif hodina <23:
    print("Dobrou noc")


