def cifra(num, string):
    count = num
    if (num > 26): count = num % 26
    splited_string = list(string)
    for i in range(0, len(splited_string)):
        if (ord(string[i]) + count > 90):
            splited_string[i] = chr(65 + (count - (91 - ord(string[i]))))
        else:
            splited_string[i] = chr(ord(string[i]) + count)
    return ''.join(splited_string)

print(cifra(3, "TECLAEMAGUEDA"))
print(cifra(25, "ESCOLASUPERIORDETECNOLOGIAEGESTAODEAGUEDA"))

        
