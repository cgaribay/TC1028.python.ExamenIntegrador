# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
   # Test case 1
   (
   [6],
   ["","[0, 1, 1, 2, 3, 5]"],
   ["La salida no cumple con el caso de prueba\nDebe salir [0, 1, 1, 2, 3, 5]."]
   ),
   # Test case 2
   (
   [10],
   ["","[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"],
   ["La salida no cumple con el caso de prueba\nDebe salir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]."]
   ),
   # Test case 3
   (
   [-100, -200, 0],
   ["", "", "", "[]"],
   ["La salida no cumple con el caso de prueba\nDebe salir Error."]
   ),
   # Test case 4
   (
   [-100, -200, 2],
   ["", "", "", "[0, 1]"],
   ["La salida no cumple con el caso de prueba\nDebe salir [0, 1]]."]
   ),
   # Test case 5
   (
   [-100, -200, 20],
   ["", "", "", "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]"],
   ["La salida no cumple con el caso de prueba para 20\n]."]
   )
]
