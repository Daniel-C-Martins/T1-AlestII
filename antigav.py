def move_right(coord_x, coord_y):
    global money
    count = "0"

    print("andando pra direita")

    for i in range(coord_y, len(map[0])):  #Percorre a matriz para a direita apenas em Y(colunas)
        end(coord_x, i):

        if map[coord_x][i].isdigit():  
            print(map[coord_x][i])
            count += map[coord_x][i]
        else:
            if count != "0":
                print(count)
            money += int(count)
            count = "0"

        if test_slash(coord_x,i):
            move_up(coord_x - 1, i)
        if test_backslash(coord_x, i):
            move_down(coord_x + 1, i)
        