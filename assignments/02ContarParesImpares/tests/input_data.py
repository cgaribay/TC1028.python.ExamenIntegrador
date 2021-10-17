# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["6", "0", "1", "2", "*"],
    ["", "", "", "", "", "PARES=3", "IMPARES=1"],
    ["La salida no cumple con el caso de prueba\nSon 3 pares y 1 impar."]
    ),
    # Test case 2
    (
    ["0", "1", "2", "3", "4", "*"],
    ["", "", "", "", "", "", "PARES=3", "IMPARES=2"],
    ["La salida no cumple con el caso de prueba\nSon 3 pares y 2 impares."]
    ),
    # Test case 3
    (
    ["0", "2", "4", "*"],
    ["", "", "", "", "PARES=3", "IMPARES=0"],
    ["La salida no cumple con el caso de prueba\nSon 3 pares y 0 impares."]
    ),
    # Test case 3
    (
    ["1", "7", "9", "*"],
    ["", "", "", "", "PARES=0", "IMPARES=3"],
    ["La salida no cumple con el caso de prueba\nSon 0 pares y 3 impares."]
    )
    ]
