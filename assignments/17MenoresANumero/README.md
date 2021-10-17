![Tec de Monterrey](../../images/logotecmty.png)
#Menores a Número
Matrices: Menores a Número

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

<div style="font-family:verdana; font-size:10px">
<h3>Problema 1: Menores a 10</h3><br>
Escribe una función que reciba una matriz como parámetro y regrese una lista con los números menores a 10 que se encuentran en la matriz. Se debe tener una función auxiliar que solicite los datos por teclado (número de renglones, número de columnas y elementos de la matriz) y genere la matriz correspondiente (lista con sublistas).
<b>Utiliza el archivo que ya viene incluido en tu entorno.</b><br><br>

Entrada:<br> 
Número de renglones (número entero)<br>
Número de columnas (número entero)<br>
Valores de la matriz (números enteros)<br>
(Se ingresa un valor por renglón y estrictamente en el orden citado).

Salida: <br>
Una lista con los números menores a 10.

Ejemplo de ejecución del programa.<br>
```
>>> 2
>>> 3
>>> 1 
>>> 25 
>>> 8
>>> 30
>>> 2
>>> 4
[1, 8, 2, 4]

>>> 2
>>> 0
[]
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
