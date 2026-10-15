#Nášteva divadla
den = str(input("Zadejte den konání akce: "))
pocet_osob = int(input("Zadejte počet osob: "))
cena_zaklad= 500
#Určení slevy pro jednotlivé skupiny + podle dne
if den=="sobota" or den=="neděle":
    student = cena_zaklad * 0.7 + 50
    senior = cena_zaklad * 0.8 + 50
    skupina = cena_zaklad * 0.75 + 50
else:
    student = cena_zaklad * 0.7
    senior = cena_zaklad * 0.8
    skupina = cena_zaklad * 0.75
#Definování funkcí pro slevy *s pomocí AI, napsáno ručně
#Odkaz na koverzaci: https://chatgpt.com/share/6ace905b-c7a0-83eb-9f97-7bac25dda2d4

def bez_sleva():
    print("")
    print("-----Výslední účtenka-----")
    if den=="sobota" or den=="neděle":
        print("Dnes je víkendová akce! (+50kč za lístek)")
    print("Nemáte slevu!")
    print(f"Cena jedné vstupenky je {cena_zaklad} Kč")
    vysledek = cena_zaklad * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def skupina_sleva():
    print("")
    print("-----Výslední účtenka-----")
    if den=="sobota" or den=="neděle":
        print("Dnes je víkendová akce! (+50kč za lístek)")
    print("Máte skupinovou slevu! (25%)")
    print(f"Cena jedné vstupenky je {skupina} Kč")
    vysledek = skupina * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def student_sleva():
    print("")
    print("-----Výslední účtenka-----")
    if den=="sobota" or den=="neděle":
        print("Dnes je víkendová akce! (+50kč za lístek)")
    print("Máte studentskou slevu! (30%)")
    print(f"Cena jedné vstupenky je {student} Kč")
    vysledek = student * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

def senior_sleva():
    print("")
    print("-----Výslední účtenka-----")
    if den=="sobota" or den=="neděle":
        print("Dnes je víkendová akce! (+50kč za lístek)")
    print("Máte seniorskou slevu!(20%)")
    print(f"Cena jedné vstupenky je {senior} Kč")
    vysledek = senior * pocet_osob
    print(f"Celková cena je {vysledek} Kč")

#Vyhodnocení
if pocet_osob <=0:
    print("Zadejte platnou hodnotu!")
elif pocet_osob >=4:
    skupina_sleva()
else:
    vek = int(input("Zadejte věk: "))   
    if  vek<=26 and vek>0:
        student_bool = str(input("Jste student? [ano/ne]: "))
        if student_bool=="ano":
            student_sleva()
        else:
            bez_sleva()

    elif vek >=65:
        senior_sleva()
    elif vek<=0: 
        print("Zadejte platnou hodnotu!")
    else:
        bez_sleva()