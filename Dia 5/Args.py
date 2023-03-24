def suma(a,b):
    return a+b

def suma2(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6))
print(suma2(5,6,7,8,19))