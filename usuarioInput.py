
def comprobarPosicion(userInput):

    from re import match
    
    if match("^[A-Z]$", userInput[0]):
        return True

    if match("^[1-10]$", userInput[0]):
        return True

    return False
