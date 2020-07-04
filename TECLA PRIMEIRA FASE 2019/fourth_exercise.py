def rotative_word(str1,str2):
    if (str1 == str2): return 0
    string_splited = list(str1)
    for i in range(0,len(str1) - 1):
        temp_list = [string_splited[len(str1) - 1]]
        for j in range(0,len(str1) - 1):
            temp_list.append(string_splited[j])
        print(temp_list)
        string_splited = temp_list
        if (temp_list == list(str2)): return i + 1
    return -1 

print(rotative_word("ESTGA", "GAEST"))
print(rotative_word("ESTGA", "EETGA"))
