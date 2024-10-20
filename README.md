# Ejercicio de Programación - Sistemas Operativos: Cálculo de Fibonacci usando Hilos y Procesos

## Integrantes
- Juan José Cortés Rodríguez | 2325109
- Johan Andrés Ceballos Tabarez | 2372229
- Miguel Felipe Casanova Cortés | 2324909

## Docente
John Alexander Sanabria Ordoñez

## Descripción

Este repositorio contiene el código para un ejercicio de programación de la clase de Sistemas Operativos. El ejercicio se enfoca en comparar el rendimiento de tres formas diferentes de calcular la secuencia de Fibonacci para cada número de un vector. El vector utilizado tiene 144 elementos, todos con el valor 33.

Las tres implementaciones son:

1. **Secuencial:** (Cálculo sin usar hilos ni procesos)
2. **Hilos (Thread):** 
3. **Procesos (Process):**

El objetivo es comparar el tiempo de ejecución de cada una de estas aproximaciones mediante múltiples ejecuciones.

## Tabla de Tiempos de Ejecución

A continuación la tabla para registrar el tiempo de ejecución de cada versión para un total de 5 ejecuciones.

<div align="center">
  
| Ejecución | Secuencial (s) | Thread (s) | Process (s) |
|-----------|----------------|------------|-------------|
| 1         |  0.0016942024230957031  |            |             |
| 2         |  0.0008387565612792969  |            |             |
| 3         |  0.0007622241973876953  |            |             |
| 4         |  0.0006053447723388672  |            |             |
| 5         |  0.0014791488647460938 |            |             |
| **Promedio** |  0.001026709875  |            |             |

</div>
(las ejecuciones se realizaron en un equipo con 12 nucleos y el promedio se hizo con los 3 valores restantes al quitar el valor max y min de las 5 ejecuciones de cada script)

