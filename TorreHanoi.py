def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return 1
    movimientos = torre_hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    movimientos += 1
    movimientos += torre_hanoi(n-1, auxiliar, destino, origen)
    return movimientos

num_discos = int(input("Ingrese el número de discos: "))
total_movimientos = torre_hanoi(num_discos, 'A', 'C', 'B')
print(f"Total de movimientos: {total_movimientos}")
