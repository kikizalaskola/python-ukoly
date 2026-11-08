#Import náhodného čísla
import random
tajne_cislo = random.randint(1, 20)
#Počet pokusů na uhodnutí čísla
limit = 5
print(f"Máš {limit} pokusů" )

tip = int(input("Zadejte hádané číslo: "))
pokusy = 1

#Hlavní smyčka


while tip != tajne_cislo and limit>0:
    print("------")
    if tip >= 1 and tip <= 20:
        if tip < tajne_cislo:
            print("Moje číslo je VĚTŠÍ!")
        else:
            print("Moje číslo je MENŠÍ!")

    else:
        print("Zadejte číslo od 1-20!")
        break

    pokusy += 1
    limit -= 1
        
    print("")
    print(f"Máš {limit} pokusů" )
    tip = int(input("Zadejte hádané číslo: "))

    if tip == tajne_cislo:  
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
    if limit<=0:
        print(f"Bohužel ti došly pokusy! Tajné číslo bylo {tajne_cislo}.")


