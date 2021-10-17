![Tec de Monterrey](../../images/logotecmty.png)
# Serie Fibonacci usando listas
## Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Diseña y codifica un programa en Python que lea la cantidad de n elementos que desea tener en la lista.
El programa debe validar que n sea mayor o igual que 0, de lo contrario lo vuelve a solicitar. Como resultado, se debe desplegar la lista con los primeros n elementos de la serie de Fibonacci.

## Entrada
Un número entero positivo que corresponde al número de términos de la serie de Fibonacci que queremos en la lista. Si el dato recibido es menor que 0, se debe volver a solicitar.

## Salidas
La lista con el número de términos de la serie de Fibonacci solicitados, uno por renglon. No uses letreros para solicitar los datos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 5
```
### Salida
```
[0, 1, 1, 2, 3]
```
### Entrada
```
>>> 9
```
### Salida
```
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```
### Entrada
```
>>> 0
```
### Salida
```
[ ]
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
