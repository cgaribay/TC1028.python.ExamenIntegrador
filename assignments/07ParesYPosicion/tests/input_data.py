# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    [5, 2, 3, 6, 1, 10],
    ["", "", "", "", "", "", "pos 0, valor 2", "pos 2, valor 6", "pos 4, valor 10"],
    ["La salida no cumple con el caso de prueba\nhay 3 números pares."]
    ),
    # Test case 2
    (
    [7, 5, 8, 20, 9, 33, 42, 56],
    ["", "", "", "", "", "", "", "", "pos 1, valor 8","pos 2, valor 20", "pos 5, valor 42", "pos 6, valor 56"],
    ["La salida no cumple con el caso de prueba\nhay 4 números pares."]
    ),
    # Test case 3
    (
    [2, 4, 10],
    ["", "", "", "pos 0, valor 4", "pos 1, valor 10"],
    ["La salida no cumple con el caso de prueba\nHay 2 números pares."]
    ),
    # Test case 4
    (
    [1, 3],
    ["", ""],
    ["La salida no cumple con el caso de prueba\nNo hay números pares."]
    )
]
