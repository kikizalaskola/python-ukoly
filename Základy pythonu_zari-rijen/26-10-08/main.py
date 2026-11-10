#Určemý souřadnice panáčka
x_panacko = int(input("Zadejte souřadnici X: "))
y_panacka = int(input("Zadejte souřadnici Y: "))
#Určení zóny
x1=2
x2=6
y1=2
y2=5

# Test jestli jsme v kolizi

if  (x_panacko>=x1 and x_panacko<=x2) and (y_panacka>=y1 and y_panacka<=y2) :
      print("Trefa!")
else :
    print("Vedle")