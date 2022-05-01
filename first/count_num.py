def countNum (firstInt, secondInt):
    if not firstInt.isnumeric() or not secondInt.isnumeric():
        return "One of numbers consist non-number symbols"    

    if len(list(firstInt)) > len(list(secondInt)):
        return firstInt
    else: 
        return secondInt

