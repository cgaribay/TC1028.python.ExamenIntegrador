# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    [2, 3],
    ["", "", "[[1, 2, 3], [4, 5, 6]]"],
    ["La salida no cumple con el caso de prueba\nChecar el caso para una matriz de 2 renglones y 3 columnas."]
    ),
    # Test case 2
    (
    [4, 4],
    ["", "", "[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]"],
    ["La salida no cumple con el caso de prueba\nChecar el caso para una matriz de 4 x 4."]
    ),
    # Test case 3
    (
    [-3, 0],
    ["", "", "Error"],
    ["La salida no cumple con el caso de prueba\nDebe mostrar el mensaje de Error."]
    )
    ]
