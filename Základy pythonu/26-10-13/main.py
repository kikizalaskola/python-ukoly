#Nášteva divadla
vek = int(input("Zadejte věk: "))
student_bool = str(input("Jste student? : "))
pocet_osob = int(input("Zadejte počet osob: "))
cena_zaklad= 500
student = cena_zaklad * 0.7
senior = cena_zaklad * 0.8
skupina = cena_zaklad * 0.75

if pocet_osob >=4:
    print("Máte skupinovou slevu!")
    print(f"Cena jedné vstupenky je {skupina} Kč")
    vysledek = skupina * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

elif  vek<=26 and student_bool=="ano":
    print("Máte studentskou slevu!")
    print(f"Cena jedné vstupenky je {student} Kč")
    vysledek = student * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

elif vek >=65:
    print("Máte seniorskou slevu!")
    print(f"Cena jedné vstupenky je {senior} Kč")
    vysledek = senior * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

else:
    print("Nemáte slevu!")
    print(f"Cena jedné vstupenky je {cena_zaklad} Kč")
    vysledek = cena_zaklad * pocet_osob
    print(f"Celková cena je {vysledek} Kč")
