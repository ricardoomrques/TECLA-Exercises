def swimming(num,round,participants):
    participants = sorted(participants)
    result = ""
    names = []
    time = []
    for i in range(0,len(participants)):
        names.append(participants[i][0:participants[i].find(' ')])
        time.append(int(participants[i][participants[i].find(' ') + 1:]))
    if (round == 1):
        for j in range(0,8):
            result += names[time.index(min(time))] + ' ' + "\n"
            names.remove(names[time.index(min(time))])
            time.remove(time[time.index(min(time))])
    elif (round == 2):
        for j in range(0, 16):
            result += names[time.index(min(time))] + ' ' + "\n"
            names.remove(names[time.index(min(time))])
            time.remove(time[time.index(min(time))])
    else:
        for j in range(0,32):
            result += names[time.index(min(time))] + ' ' + "\n"
            names.remove(names[time.index(min(time))])
            time.remove(time[time.index(min(time))])

    return result

        

print(swimming(16,1,["Pedro 100", "Gaspar 99", "Antonio 95", "Carlos 101", "Andre 102", "Luis 98", "Bruno 96", "Jose 102",
 "Gil 96", "Mario 102", "Sergio 98", "Joao 100", "Joaquim 93", "Valter 94", "Hugo 95", "Miguel 101"]))

print(swimming(10,1,["Adriana 80", "Clara 95", "Ana 78", "Carla 100", "Vera 77", "Andreia 105", "Petra 79", "Rita 88", "Daniela 93",
"Eduarda 80"]))