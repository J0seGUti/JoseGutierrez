import random

# Cara y Sello 

num=random.randint(1, 2)

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
    







    