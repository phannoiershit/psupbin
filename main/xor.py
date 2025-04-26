def xor(a,b):
    if type(a)!="bool" or type(b)!="bool":
        raise SyntaxError("Must a boolean")
    elif a == b:
        return False
    else:
        return True
