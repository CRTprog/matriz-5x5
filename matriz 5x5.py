
matriz = []


for i in range(5):
    fila = []
    for j in range(5):
        valor = float(input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): "))
        fila.append(valor)
    matriz.append(fila)

print("\nContenido de la matriz:")
for fila in matriz:
    for valor in fila:
        print(f"{valor:}", end="\t")  
    print()  