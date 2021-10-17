# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["3","1","2","4","5"],
        ["","","","","","[11]"],
        "Error"
    ),   
    (
        ["1","4","7","3","4","5"],
        ["","","","","","","[7, 3, 4, 5]"],
        "Error"
    ),  
     (
        ["-1","1"],
        ["","","Error"],
        "Error"
    )
]
