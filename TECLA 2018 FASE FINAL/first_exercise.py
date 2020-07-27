def rabbit_chickens(x,y):
    return str(int(2*x - 0.5*y)) + "\n" + str(int(-x + 0.5*y))

print(rabbit_chickens(35,94))
print(rabbit_chickens(4,12))