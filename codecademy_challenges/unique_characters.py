def unique_characters(string_in):
    if string_in == "":
        return "Error - empty string"

    string = string_in.lower()
    chars = list(string)
    index = 0
    result = True

    for char in chars:
        char = char.lower()
        current = char
        current_index = 0
        for char in chars:
            if current_index == index:
                continue
            elif current == char:
                result = False
            elif result == False:
                break
            else:
                 result = True
            current_index += 1
        index += 1
    
    return result



print(unique_characters("Tulip"))

