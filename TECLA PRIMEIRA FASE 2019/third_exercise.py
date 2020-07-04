def sum_digits(x):
    x = str(x)
    result = 0
    for i in range(0,len(str(x))):
        if (int(x[i]) % 2 == 0): result += int(x[i]) * 2
        else: result += int(x[i])
    return result

print(sum_digits(362))
print(sum_digits(534179))