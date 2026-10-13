#Nášteva divadla

pocet_osob = int(input("Zadejte počet osob: "))
cena_zaklad= 500
#Určení slevy pro jednotlivé skupiny

student = cena_zaklad * 0.7
senior = cena_zaklad * 0.8
skupina = cena_zaklad * 0.75
#Definování funkcí pro slevy *s pomocí AI, napsáno ručně

def bez_sleva():
    print("Nemáte slevu!")
    print(f"Cena jedné vstupenky je {cena_zaklad} Kč")
    vysledek = cena_zaklad * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def skupina_sleva():
    print("Máte skupinovou slevu!")
    print(f"Cena jedné vstupenky je {skupina} Kč")
    vysledek = skupina * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def student_sleva():
    print("Máte studentskou slevu!")
    print(f"Cena jedné vstupenky je {student} Kč")
    vysledek = student * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def senior_sleva():
    print("Máte seniorskou slevu!")
    print(f"Cena jedné vstupenky je {senior} Kč")
    vysledek = senior * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

#Vyhodnocení slevy

if pocet_osob >=4:
    skupina_sleva()
else:
    vek = int(input("Zadejte věk: "))   
    if  vek<=26:
        student_bool = str(input("Jste student? [ano/ne]: "))
        if student_bool=="ano":
            student_sleva()
        else:
            bez_sleva()

    elif vek >=65:
        senior_sleva()

    else:
        bez_sleva()