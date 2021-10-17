![Tec de Monterrey](../../images/logotecmty.png)
# Pares y posición
### Tema Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que primero lea la cantidad de elementos que vas a ingresar en la lista y después acepte cada uno de los elementos. Todos los datos que se ingresan deben ser números enteros.
Posteriormente, el programa debe revisar la lista, y para cada uno de los valores pares que encuentre mostrar un mensaje con la posición y el valor del número par usando un formato que se describe más adelante.

## Entrada
Un número entero que representa la cantidad de valores que tiene la lista, asi como cada uno de los valores de la lista.

## Salida
Un mensaje para cada uno de los números pares encontrados en la lista. El mensaje debe tener el formato:
```
pos XX, valor XX
```
Observa que va la palabra ``pos`` seguida de un ``número``, después una ``coma``, un `espacio`, luego la palabra ``valor`` y luego otro ``número``. 
 
## Ejemplo de ejecución del programa:
### Entrada
```
>>>5
>>>1
>>>2
>>>3
>>>4
>>>5
```
### Salida
```
pos 1, valor 2
pos 3, valor 4
```
No uses letreros para pedir los datos y diseña los letreros de salida iguales a los del ejemplo.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
