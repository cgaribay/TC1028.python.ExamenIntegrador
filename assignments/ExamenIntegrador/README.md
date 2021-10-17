![Tec de Monterrey](../../images/logotecmty.png)
# Examen Integrador

Realiza un programa en Python que cargue la información de los archivos productos.csv, vendedores.csv y ventas.csv a las matriz de productos, vendedores y ventas (**Esto NO lo tienes que hacer, ya viene incluido en el código de inicio en github**). Posteriormente crea y manda llamar una función llamada **revisar_metas**. Esta función deberá preguntar el nombre de un vendedor, si el vendedor no existe imprimir el mensaje "Error" y volver a preguntar el nombre. Si el vendedor SI existe, calcular el dinero generado por las ventas del vendedor y, si ese dinero es mayor o igual a la meta de ese vendedor, entonces se debe imprimir el mensaje "Felicidades por alcanzar la meta de ventas". Si no se ha alcanzado esa meta deberás imprimir un mensaje informando la cantidad de dinero que le falta al vendedor para llegar a la meta.

La meta se encuentra en el archivo de vendedores.csv y se guarda en la matriz de vendedores cuando se carga ese archivo a la matriz.

## Entrada
El nombre del vendedor, en mayúsculas o minúsculas.

## Salida
El mensaje "Felicidades por alcanzar la meta de ventas", si el vendedor alcanzó la meta o el mensaje "Te falta X para alcanzar la meta de ventas" si aún no se alcanza la meta.

## Ejemplo de ejecución del programa
```
>>> a
>>> Error
>>> luis perez
>>> Felicidades por alcanzar la meta de ventas
```

```
>>> b
>>> Error
>>> CaRlOs LopeZ
>>> Te falta 420 para alcanzar la meta de ventas
```


**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
