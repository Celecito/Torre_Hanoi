from typing import Any

def torre_hanoi(n: int, origen: str, destino: str, auxiliar: str) -> int:
    """
    Resuelve el problema de la Torre de Hanoi de forma estrictamente recursiva.
    
    Args:
        n (int): Número de discos.
        origen (str): Torre de origen.
        destino (str): Torre de destino.
        auxiliar (str): Torre auxiliar.
    
    Returns:
        int: Número total de movimientos realizados.
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return 1
    movimientos = torre_hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    movimientos += 1
    movimientos += torre_hanoi(n-1, auxiliar, destino, origen)
    return movimientos

def pedir_num_discos() -> int:
    """
    Solicita al usuario el número de discos y valida la entrada.
    
    Returns:
        int: Número de discos válido (entre 1 y 20).
    Raises:
        ValueError: Si la entrada no es válida.
    """
    while True:
        try:
            entrada: Any = input("Ingrese el número de discos (1-20): ")
            num_discos = int(entrada)
            if not (1 <= num_discos <= 20):
                raise ValueError("El número debe estar entre 1 y 20.")
            return num_discos
        except ValueError as ve:
            print(f"Entrada inválida: {ve}")
        except TypeError:
            print("Tipo de dato inválido. Debe ingresar un número entero.")

if __name__ == "__main__":
    num_discos = pedir_num_discos()
    total_movimientos = torre_hanoi(num_discos, 'A', 'C', 'B')
    print(f"Total de movimientos: {total_movimientos}")

    # Pruebas básicas
    print("\nPruebas básicas de cantidad de movimientos:")
    for n in range(1, 5):
        esperado = 2 ** n - 1
        resultado = torre_hanoi(n, 'A', 'C', 'B')
        print(f"Discos: {n} | Movimientos esperados: {esperado} | Movimientos calculados: {resultado}")
