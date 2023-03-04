import random

print("Bienvenido a D1...\n"
      "Estamos de aniversario y te obsequiaremos un descuento segun el valor de tu compra.\n"
      "Ésta debe ser mayor a 50.000 y dependemos de tu suerte.\n""\n"
      "El descuento dependerá del color de la bolita que salga en el sorteo\n"
      "\n"
      "Bolita roja obtienes 10%\n"
      "Bolita azul obtienes un 30%\n"
      "Bolita amarilla obtienes un 50%\n"
      "Bolita blanca te llevas tu compra gratis\n")

totalCompra = 0.0
cantidadProductos = 0
valorFinal = 0


while True:
    precioProducto = float(input("Por favor ingrese el precio del producto a registrar o oprima 0 para finalizar: "))
    if precioProducto == 0:
        break
        
    cantidadProducto = int(input("por favor ingrese la cantidad de productos a registar: "))    
    totalCompra += precioProducto * cantidadProducto
    cantidadProductos += cantidadProducto

   

bolita = random.choice(["roja", "azul", "amarilla", "blanca\n"])


if totalCompra >= 50000:
    if bolita == "roja":
        descuento = totalCompra * 0.1
        valorFinal = totalCompra - descuento
        print("\n")
        print("Felicidades! Salio la bolita roja, obtuviste un descuento del 10%.\n"
              "Debes pagar: ", valorFinal,"\n")
        
    elif bolita == "azul":
        descuento = totalCompra * 0.3
        valorFinal = totalCompra - descuento
        print("\n")
        print("Felicidades! Salio la bolita azul, obtuviste un descuento del 30%.\n"
              "Debes pagar: ", valorFinal,"\n")
        
    elif bolita == "amarilla":
        descuento = totalCompra * 0.5
        valorFinal = totalCompra - descuento
        print("\n")
        print("Felicidades! Salio la bolita amarilla, obtuviste un descuento del 50%.\n"
              "Debes pagar: ", valorFinal,"\n")
        
    elif bolita == "blanca":
        descuento = totalCompra
        valorFinal = 0
        print("\n")
        print("Felicidades! Salio la bolita blanca te llevas tu compra gratis.", valorFinal,"\n")
        
    else:
        print("Lo sentimos, no obtuviste descuento en esta ocasión.\n")
        
else:
    print("Lo sentimos, tu compra debe ser mayor a 50.000 para obtener algún descuento.\n")

valorPagado = float(input("Por favor ingrese el valor con el que el cliente pagará: "))
print("\n")

cambio = valorPagado - valorFinal

print("Gracias por tu compra.\n"      
      "Cantidad de productos adquiridos:", cantidadProductos, "\n"
      "Valor de la compra:", totalCompra, "\n"
      "Tu descuento fue: ",descuento,"\n"
      "Tu cambio es",cambio,"\n")