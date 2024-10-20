#
# Nombre: FiboWorkerSequential33.py
# Descripción: Este codigo procesa de forma secuencial  cada uno de los 144 elementos del vector que se inicializa con 33 para calcular el fibonacci de cada uno, se guarda el resultado en la misma posición y se guarda el tiempo que tarda en realizar la tarea. 
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
# Modificado por: Juan José Cortés Rodríguez - juan.jose.cortes@correounivalle.edu.co
# Fecha: 2024-10-19
#

from time import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fiboWorkerSequential():
    tiempo  = time()
    vector33 = [33]*144
    print("Vector sin modificar:", list(vector33))
    for n in range(144):
        vector33[n] = fibo(vector33[n])
        print(f"El fibonacci del número  33 ubicado en la posicion {n} es {vector33[n]}")

    print(f"El proceso tomo {time() - tiempo} segundos")
    print("Vector modificado:", list(vector33))

fiboWorkerSequential()
