![Tec de Monterrey](../../images/logotecmty.png)
# Centro Matriz
Matrices Centro Matríz

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

<div style="font-family:verdana; font-size:10px">
<h3>Centro de la matriz</h3><br>
Escribe una función centro_matriz que pregunta el número de renglones y número de columnas de una matriz, después pregunta cada valor entero de la matriz y regresa el centro de la matriz quitando el primer renglón, primera columna, último renglón y última columna.<br><br>

Entrada<br>
Dos números enteros que son el número de renglones y el número de columnas (en ese orden).
Los números enteros que son elementos de la matriz.
(Cada valor en un renglón y estrictamente en el orden citado).

Salida<br>
La matriz que corresponde al centro de la matriz (es decir la matriz original sin el primer y último renglón y sin la primera y última columna).

Ejemplos de ejecución del programa.<br>
```
>>> 1
>>> 1
>>> 1
[ ]

>>> 3
>>> 3
>>> 1
>>> 1
>>> 1
>>> 2
>>> 2
>>> 2
>>> 3
>>> 3
>>> 3
[ [2] ]

>>> 0
>>> 3
[ ]
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
