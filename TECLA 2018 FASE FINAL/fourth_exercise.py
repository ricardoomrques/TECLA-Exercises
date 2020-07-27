def calls(num, call_list):
    string = ""
    complete_tuple = ()
    temp_num = [int(call_list[0][0:9])]
    temp_cost = [int(call_list[0][10:])]
    for i in range(1, num):
        if (int(call_list[i][0:9]) not in temp_num):
            temp_num.append(int(call_list[i][0:9]))
            temp_cost.append(int(call_list[i][10:]))
        else:
            temp_cost[temp_num.index(int(call_list[i][0:9]))] = int(temp_cost[temp_num.index(int(call_list[i][0:9]))]) + int(call_list[i][10:])
    for i in range(0, len(temp_num)):
        tup = (temp_num[i],temp_cost[i])
        complete_tuple += (tup,)
    complete_tuple = sorted(complete_tuple)
    for i in range(0,len(complete_tuple)):
        string += str(complete_tuple[i][0]) + " " + str(round((complete_tuple[i][1] / 60) * 0.342,2)) + "\n"
    return string


print(calls(3, ["673849273 30", "563782736 60", "673849273 40"]))
print(calls(5,["676388273 120","566763566 10", "676388273 100", "676388273 90", "898998273 300"]))
