#
# Nombre: FiboWorkerProcess33.py
# Descripción: Este script define un hilo que se encarga de calcular la posicion 'n' en la serie de Fibonacci.
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
# Modificado por: Miguel Casanova - miguel.felipe.casanova@correounivalle.edu.co
# Fecha: 2024-10-19
#

from time import time
import multiprocessing
import sys

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

class FiboWorker(multiprocessing.Process):
    def __init__(self, shared_array, inicio, fin, pid):
        multiprocessing.Process.__init__(self)
        self.shared_array = shared_array
        self.inicio = inicio
        self.fin = fin
        self._pid = pid

    def run(self):
        for i in range(self.inicio, self.fin):
            self.shared_array[i] = fibo(self.shared_array[i])
        print(f"[{self.pid}] Procesó elementos {self.inicio} a {self.fin - 1}")

def main():
    max_fibo = 33
    if len(sys.argv) > 1:
        max_fibo = int(sys.argv[1])
    
    num_cpus = multiprocessing.cpu_count()  # CPUs disponibles
    procesos = []  # Vector de procesos
    
    vector33 = multiprocessing.Array('i', [33] * 144)
    print("Vector sin modificar:", list(vector33))
    segmento = len(vector33) // num_cpus
    ts = time()  # Se toma tiempo
    
    for x in range(num_cpus):  # Ciclo para crear trabajadores
        inicio = x * segmento
        fin = (x + 1) * segmento if x != num_cpus - 1 else len(vector33)
        print(f"Trabajador {x} comienza")
        worker = FiboWorker(vector33, inicio, fin, x)
        worker.start()
        procesos.append(worker)

    for x in range(num_cpus):  # Ciclo para esperar por trabajadores
        print(f"Esperando por trabajador {x}")
        procesos[x].join()

    print("Vector modificado:", list(vector33)) 
    print(f"Tomó {time() - ts} segundos")


if __name__ == "__main__":
    main()

