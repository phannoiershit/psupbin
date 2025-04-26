def xor(a,b):
    if type(a)!="bool" or type(b)!="bool":
        raise SyntaxError("Must a boolean")
    elif a == b:
        return False
    else:
        return True
def orb(a,b):
    if not a in (0, 1) or not b in (0, 1):
        raise SyntaxError("Binaries must be 0 or 1")
    elif a == 0 and b == 0:
        return 0
    else:
        return 1

def andb(a,b):
    if not a in (0, 1) or not b in (0, 1):
        raise SyntaxError("Binaries must be 0 or 1")
    elif a == 1 and b == 1:
        return 1
    else:
        return 0

def xorb(a,b):
    if not a in (0, 1) or not b in (0, 1):
        raise SyntaxError("Binaries must 0 or 1")
    elif a == b:
        return 0
    else:
        return 1

def nob(a):
    if not a in (0, 1):
        raise SyntaxError("Binaries must 0 or 1")
    elif a is 1:
        return 0
    else:
        return 1
    
