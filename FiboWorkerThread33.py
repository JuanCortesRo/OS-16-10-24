from threading import Thread
from time import time
from multiprocessing import cpu_count

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

class FiboWorker(Thread):
    def __init__(self, vector, start_idx, end_idx):
        super().__init__()
        self.vector = vector
        self.start_idx = start_idx
        self.end_idx = end_idx

    def run(self):
        for i in range(self.start_idx, self.end_idx):
            n = self.vector[i]
            resultado = fibo(n)
            print(f"[{i}] Fibonacci de {n} es {resultado}")
            self.vector[i] = resultado

def main():
    vector33 = [33] * 144 

    print("Vector inicial:", vector33)
    num_workers = cpu_count()
    chunk_size = len(vector33) // num_workers
    workers = []

    for i in range(num_workers):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i != num_workers - 1 else len(vector33)
        worker = FiboWorker(vector33, start_idx, end_idx)
        workers.append(worker)

    ts = time()

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    print(f"Tiempo total: {time() - ts:.4f} segundos")
    print("Vector resultante:", vector33)
if __name__ == "__main__":
    main()
