import random

print("Bienvenido a Sumpermercados Noé...\n"
      "Estamos de aniversario y te obsequiamos un descuento en el valor de tu compra.\n"
      "Ésta debe ser mayor a 50.000 y dependemos de tu suerte.\n""\n"
      "El descuento dependerá del color de la bolita que salga en el sorteo\n"
      "\n"
      "Bolita roja obtienes 10%\n"
      "Bolita azul obtienes un 30%\n"
      "Bolita amarilla obtienes un 50%\n"
      "Bolita blanca te llevas tu compra gratis\n")

valorCompra = float(input("Por favor ingresa el valor de tu compra: "))

bolita = random.choice (["roja", "azul", "amarilla", "blanca"])

if valorCompra > 50000:
    if bolita == "roja":
        descuento = valorCompra * 0.1
        valorFinal = valorCompra - descuento
        print("Felicidades! Salio la bolita roja, obtuviste un descuento del 10%.\n"
              "Debes pagar: ",+valorFinal)
        
    elif bolita == "azul":
        descuento = valorCompra * 0.3
        valorFinal = valorCompra - descuento
        print("Felicidades! Salio la bolita azul, obtuviste un descuento del 30%.\n"
              "Debes pagar: ",+valorFinal)
        
    elif bolita == "amarilla":
        descuento = valorCompra * 0.5
        valorFinal = valorCompra - descuento
        print("Felicidades! Salio la bolita amarilla, obtuviste un descuento del 50%.\n"
              "valor a pagar: ",+valorFinal)
        
    elif bolita == "blanca":
        descuento = valorCompra
        valorFinal = 0
        print("Felicidades! Salio la bolita blanca te llevas tu compra gratis.",+valorFinal)
        
    else:
        print("Lo sentimos, no obtuviste descuento en esta ocasión.")
        
else:
    print("Lo sentimos, tu compra debe ser mayor a 50.000 para obtener algún descuento.")