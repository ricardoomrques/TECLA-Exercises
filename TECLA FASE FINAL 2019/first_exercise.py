def run(comp, num_laps, fuel, safety):
    comp *= num_laps
    fuel = (comp * fuel) / 100
    fuel += (safety / 100) * fuel
    return round(fuel,2)

print(run(5,30,20,12)) 
print(run(10,25,30,15))