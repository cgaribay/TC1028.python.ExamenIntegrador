![Tec de Monterrey](../../images/logotecmty.png)
# cuenta pares e impares
## Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Diseña e implementa un programa que determine la cuenta de valores pares e impares de los elementos de una lista de números enteros que recibirá en su entrada. Los valores los introduce el usuario uno por uno, se van almacenando en una lista y posteriormente se analizará la lista para determinar cuantos valores pares e impares posee. Consideramos al 0 como par.

## Entrada
Cero o más valores enteros, uno en cada renglón. Finaliza la captura con un *.

## Salida
Se despliega el número de pares e impares que tiene la lista con el siguiente formato: 
PARES=3 o IMPARES=2 cada uno en un renglón. 
El desplegado de la salida consiste en la palabra PARES seguida de un = y luego un número que representa el número de pares en la lista; posteriormente la palabra IMPARES, seguida de un = y luego el número que representa el número de impares que hay en la lista. Cada mensaje en un renglón y en ese orden.

## Ejemplo de ejecución del programa
### Entrada
```
>>> 6
>>> 0
>>> 1
>>> 2
>>> *
```
### Salida
```
PARES=3
IMPARES=1
```
### Entrada
```
>>> *
```
### Salida
```
PARES=0
IMPARES=0
````


**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
