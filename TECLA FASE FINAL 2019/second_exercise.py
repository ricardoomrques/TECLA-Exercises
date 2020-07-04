import math

def golden_number(c,l):
    if ((c / l) - (1 + math.sqrt(5) / 2) < 0.01): return "sim"
    return "nao"

print(golden_number(3.25,2))
print(golden_number(1.35,0.28))
