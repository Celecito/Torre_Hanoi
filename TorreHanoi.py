def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    torre_hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    torre_hanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso con 3 torres: A (origen), B (auxiliar), C (destino)
num_discos = int(input("Ingrese el número de discos: "))
torre_hanoi(num_discos, 'A', 'C', 'B')