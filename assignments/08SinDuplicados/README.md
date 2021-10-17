![Tec de Monterrey](../../images/logotecmty.png)
# Lista sin elementos duplicados
### Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que reciba del usuario una lista, la despliegue y despliegue otra lista con los elementos de la lista original, pero sin elementos duplicados. 

## Entradas
Se recibe un número entero positivo mayor a cero correspondiente al número de elementos que el usuario ingresará.
Se reciben uno a uno y por renglón, los elementos de la lista (strings o numeros de acuerdo al número recibido anteriormente). No uses letreros para solicitar los datos al usuario.

## Salidas
Si el valor correspondiente al número de elementos que tendrá la lista es ```0``` o ```negativo``` se deberá mandar el mensaje ```“Error”```. Si el valor recibido es mayor a 0, se despliega la lista original (después de haber recibido los datos). Posteriormente se despliega la lista sin duplicados.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 4
>>> Pedro
>>> Gerardo
>>> Hugo
>>> Pedro
```
### Salida
```
['Pedro', 'Gerardo', 'Hugo', 'Pedro']
['Pedro', 'Gerardo', 'Hugo']
```
### Entrada
```
>>> 0
```
### Salida
```
"Error"
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
