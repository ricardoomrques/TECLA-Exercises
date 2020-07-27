def votes(num, votes):
    temp = list(votes)
    if (temp.count("A") == temp.count("B")): return "Empate"
    elif (temp.count("A") > temp.count("B")): return "A"
    else: return "B"

print(votes(6,"ABBABA"))
print(votes(8,"AABABAAA"))