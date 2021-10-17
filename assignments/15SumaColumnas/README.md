![Tec de Monterrey](../../images/logotecmty.png)
# Suma columnas
Matrices suma columnas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

<div style="font-family:verdana; font-size:10px">
<h3>Suma columnas de una matriz</h3>
Escribe un programa que pregunte el número de renglones y número de columnas de una matriz, después pregunte cada número de la matriz y regrese una lista con la suma de cada columna de la matriz.
<b>Utiliza el archivo que se te provee en el entorno para implementar tu ejercicio </b>

Entrada:<br>
Dos números enteros que son el número de renglones y el número de columnas, uno por renglón y en ese orden.
La cantidad de números enteros que corresponderán a los elementos de la matriz, en total la cantidad de números a recibir es la multiplicación de los dos primeros números recibidos.

Salida:<br>
Lista con la suma de cada columna de la matriz. 
Si alguno de los números recibidos correspondientes a la cantidad de renglones o de columnas son menores a 1, desplegar el mensaje: "Error".

Ejemplo de ejecución del programa
```plaintext
>>> 3
>>> 1
>>> 2
>>> 4
>>> 5
[11]

>>> 0
>>> 4
Error

>>> 2
>>> 2
>>> 4
>>> -1
>>> 3
>>> 6
[7 5]
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
