competidores = {}

num_competidores = int(input("Ingrese la cantidad de participantes en el concurso de natacion: "))

for i in range(1, num_competidores + 1):
    nombre = input(f"Ingrese el nombre del competidor {i}: ")
    tiempo = float(input(f"Ingrese el tiempo de {nombre}: "))
    competidores[nombre] = tiempo

print("\nTiempos registrados:")
for nombre, tiempo in competidores.items():
    print(f"{nombre}: {tiempo}")

ganador = min(competidores, key=competidores.get)
print(f"\nEl ganador es: {ganador} con un tiempo de natacion {competidores[ganador]} minutos")
