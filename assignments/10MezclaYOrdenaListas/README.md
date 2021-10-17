![Tec de Monterrey](../../images/logotecmty.png)
# Mezcla y ordena listas
## Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Desarrolla un programa que permita obtener una lista ordenada de menor a mayor a partir de dos listas. Los valores individuales de las listas de entrada los captura el usuario uno por uno y posteriormente se unen ambas listas para obtener una sola lista ordenada de menor a mayor.

## Entradas
Cero o más valores enteros, uno en cada renglón por cada lista. Finaliza la captura de cada lista individual con un *.

## Salidas
Se despliegan las dos listas iniciales y la lista final ordenada con el siguiente formato mostrado en el ejemplo.

## Ejemplo de ejecución del programa
### Entrada
```
>>>3
>>>1
>>>4
>>>5
>>>*
>>>2
>>>9
>>>6
>>>1
>>>3
>>>*
```
### Salida
```
L1=
[3, 1, 4, 5]
L2=
[2, 9, 6, 1, 3]
LORDENADA=
[1, 1, 2, 3, 3, 4, 5, 6, 9]
```
### Entrada
```
>>> *
>>> *
```
### Salida
```
L1=
[]
L2=
LORDENADA=
[]
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
