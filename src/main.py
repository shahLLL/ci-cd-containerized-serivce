def count_o(input_string):
    # This is a simple function that counts the number of O's (both small and upper case) in a provided input string
    output_string = "The number of O's in the provided input string: "
    type_error_string = "The provided input is not a string!"
    
    if type(input_string) is not str:
        return type_error_string
    
    counter = 0
    to_lower_input_string = input_string.lower()
    for c in to_lower_input_string:
        if c == 'o':
            counter = counter + 1
    
    return output_string + str(counter)
        

#print(count_o("Hello, World!"))
#print()