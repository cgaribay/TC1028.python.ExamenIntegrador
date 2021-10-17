![Tec de Monterrey](../../images/logotecmty.png)
# Determinante
Encontrar determninante

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

Desarrolla una función en Python que reciba  una matriz de números enteros de tamaño 2x2 y calcule su determinante.
El determinante de una matriz es un número real asociado a una matriz cuadrada. 
Para una matriz de tamaño 2x2 el determinante se calcula de la siguiente forma:
 | a   b |
 | c   d |
det = a*d - c*b
El programa debe construir la matriz y posteriormente calcular el determinante con la función desarrollada. <b> Utiliza el archivo que encontrarás en el entorno.</b>

En caso de que la matriz no corresponda a una matriz de 2X2 deberá desplegar el mensaje "La matriz no es una matriz de 2x2".
Nota: Se debe incluir una función auxiliar que pida por teclado los valores de los dos renglones de la matriz y la cree. 

Entrada: <br>
Los renglones de la matriz, separando los valores por espacios. (2 valores por renglón, 2 renglones)
Se sugiere utilizar la función <b>split</b> para generar una lista a partir de los datos dados en cada renglón.<br>

Salida: <br>
El valor correspondiente al determinante de la matriz.  En caso de entradas erróneas el mensaje "La matriz no es una matriz de 2x2".<br>

Ejemplo de ejecución del programa<br>
```
>>> 1 2
>>> 3 4
-2

>>> 1 2 1
>>> 1 2 4

La matriz no es una matriz de 2x2
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
