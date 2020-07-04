def neighbours(lin,col,matriz):
    count = 0
    string = ""
    places_visited = []
    while (count < lin * col):
        index_lin = 0
        index_col = 0
        neighbours_list = []
        minimo = 99999
        for i in range(0,len(matriz)):
            for j in range(0,len(matriz[0])):
                if (matriz[i][j] < minimo and matriz[i][j] not in places_visited): 
                    minimo = matriz[i][j]
                    index_lin = i
                    index_col = j
        count += 1
        places_visited.append(minimo)
        if (index_lin - 1 >= 0 and index_col - 1 >= 0): neighbours_list.append(matriz[index_lin - 1][index_col - 1])
        if (index_lin + 1 < lin and index_col + 1 < col): neighbours_list.append(matriz[index_lin + 1][index_col + 1])
        if (index_lin - 1 >= 0 and index_col + 1 < col): neighbours_list.append(matriz[index_lin - 1][index_col + 1])
        if (index_lin + 1 < lin and index_col - 1 >= 0): neighbours_list.append(matriz[index_lin + 1][index_col - 1])
        if (index_lin - 1 >= 0): neighbours_list.append(matriz[index_lin - 1][index_col])
        if (index_lin + 1 < lin): neighbours_list.append(matriz[index_lin + 1][index_col])
        if (index_col - 1 >= 0): neighbours_list.append(matriz[index_lin][index_col - 1])
        if (index_col + 1 < col): neighbours_list.append(matriz[index_lin][index_col + 1])
        neighbours_list.sort()
        string += str(minimo) + ": "
        for k in range(0,len(neighbours_list)):
            string += str(neighbours_list[k]) + " "
        string += "\n"
    return string

print(neighbours(3,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(neighbours(4,3,[[21,23,25],[22,24,26],[27,29,31],[28,30,32]]))
print(neighbours(2,5,[[52,56,58,62,64],[53,55,59,61,63]]))




        