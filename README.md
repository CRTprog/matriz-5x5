asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]   

def mostrar_estado_sala():
    print("Estado de la sala:")
    for fila in range(3):
        for columna in range(4):
            print(asientos[fila][columna], end=' ')
        print()  
fila_usuario = int(input("Ingrese fila (0 a 2): "))
columna_usuario = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila_usuario < 3 and 0 <= columna_usuario < 4:
    asientos[fila_usuario][columna_usuario] = 1
    print("Reserva exitosa.")               
else:
    print("Índices no válidos. Por favor, elija números adecuados.")    

mostrar_estado_sala() 
