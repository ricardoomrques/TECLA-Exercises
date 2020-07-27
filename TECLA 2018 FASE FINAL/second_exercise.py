def water_price(day,c):
    result = 0.25 * day
    if (c <= 5): result += c * 0.5
    elif (5 < c <= 10): result += 5 * 0.5 + (c - 5) * 1.5
    elif (10 < c <= 25): result += 5 * 0.5 + 5 * 1.5 + (c - 10) * 2.1
    else: result += 5 * 0.5 + 5 * 1.5 + 15 * 2.1 + (c - 25) * 2.7
    return round(result * 1.06,2)

print(water_price(32,27))
print(water_price(30,15))