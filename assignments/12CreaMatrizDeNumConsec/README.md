![Tec de Monterrey](../../images/logotecmty.png)
# Matriz de numeros consecutivos
### Tema: matrices (listas de listas)

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que cree una matriz de n filas y m columnas y la llene por números consecutivos por renglón comenzando con el valor 1.

## Entradas
Dos números enteros mayores o iguales a 2 que representarán el numero de renglones n (número de listas) y el número de columnas m (numero de elementos en cada lista), en ese orden. Si alguno de los números recibidos no es mayor o igual a 2, se despliega el mensaje "Error"

## Salida
La matriz de nxm llena con números consecutivos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 3
>>> 2
```
### Salida
```
[ [1, 2], [3, 4], [5, 6] ]
```
### Entrada
```
>>> 3
>>> 3
```
### Salida
```
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
```
### Entrada
```
>>> 1
>>> -3
```
### Salida
```
Error
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
