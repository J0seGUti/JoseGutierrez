num_notas = int(input("Por favor ingrese la cantidad de notas a evaluar: "))

notas = []
for i in range(1, num_notas + 1):
    nota = float(input(f"Ingrese la nota {i}: "))
    while nota < 0.0 or nota > 5.0:
        nota = float(input(f"Ingrese una nota válida (entre 0.0 y 5.0) para la nota {i}: "))
    notas.append(nota)

promedio = sum(notas) / num_notas

if promedio < 3.0:
    resultado = "Reprobó"
    nota_final = 0.0
elif promedio < 4.0:
    resultado = "Pasó raspando"
    nota_final = 3.5
else:
    resultado = "Aprobó con buenos resultados"
    nota_final = 5.0

print(f"\nEl promedio de las notas ingresadas es: {promedio:.2f}")
print(f"El resultado final es: {resultado}")
print(f"La nota final es: {nota_final}")
