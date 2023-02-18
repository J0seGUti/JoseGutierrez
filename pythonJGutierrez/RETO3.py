import random

# Craps
print("En este juego se lanzan dos dados""\nSe gana si se obtiene un par de unos en los dados"
"\nSe gana si se obtiene un total de tres en los dados"
"\nSe gana si se obtiene un total de once en los dados"
"\nSe gana si se obtiene dos o doce en los dados"
"\nSe gana si se obtiene un total de siete en los dados")
num=random.randint(1, 6)

if num==1:
    moneda="cara"
if num==2:
    moneda="sello"

print("Por favor seleccione una opcion" "\ncara o sello")
resultado=input()

if resultado==num:
    print("GANASTE EL RESULTADO ES CARA")

else:
    print("PERDISTE EL RESULTADO ES SELLO")