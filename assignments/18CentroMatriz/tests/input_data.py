# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1","1","1"],
        ["","","","[]"],
        "Error"
    ),   
    (
        ["3","3","1","1","1","2","2","2","3","3","3"],
        ["","","","","","","","","","","","[[2]]"],
        "Error"
    ),  
     (
        ["0","3"],
        ["","","[]"],
        "Error"
    )
]
