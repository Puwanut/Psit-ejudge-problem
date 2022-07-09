"""ValidVar"""
def checkvalid(amount):
    """Check the correctness of variable names"""
    for _ in range(amount):
        var_name = input()
        print("Invalid" if is_invalid(var_name) else "Valid")

def is_invalid(name):
    """Return True if name is Invalid"""
    name = name.strip()
    if name[0] in "0123456789":
        return True
    if name in "if else elif while for True False continue break \
                return is in and or from as pass not def None".split():
        return True
    for char in name:
        if char.lower() not in "abcdefghijklmnopqrstuvwxyz_0123456789":
            return True
    return False

checkvalid(int(input()))
