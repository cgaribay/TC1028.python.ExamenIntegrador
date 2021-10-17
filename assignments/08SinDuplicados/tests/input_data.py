# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    [6, "Pedro", "Gerardo", "Hugo", "Pedro", "Marcela", "Pedro"],
    ["","","","","","","","['Pedro', 'Gerardo', 'Hugo', 'Pedro', 'Marcela', 'Pedro']", "['Pedro', 'Gerardo', 'Hugo', 'Marcela']"],
    ["La salida no cumple con el caso de prueba\nEn la segunda lista debes quitar a Pedro, porque está repetido."]
    ),
    # Test case 2
    (
    ["3", "1", "2", "3"],
    ["", "", "", "", "['1', '2', '3']", "['1', '2', '3']"],
    ["La salida no cumple con el caso de prueba\nDebe marcar Error porque has introducido un número negativo."]
    ),
    # Test case 2
    (
    [-3],
    ["", "Error"],
    ["La salida no cumple con el caso de prueba\nLa segunda lista debe ser igual a la primero porque no hay repetidos."]
    )
    ]
