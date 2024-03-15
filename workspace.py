import os

#Variáveis globais importantes
map = []
money = 0

#Funções de leitura do mapa

#Função responsável por ler o mapa.txt para uma matriz
def read_map():
    with open("Maps\map50.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
        archive_lines = archive.readlines()
        
    for lines in archive_lines:    #"For" responsável por colocar as linhas na matriz
        map_lines = []
        for i in lines:             
            if i != "\n":
                map_lines.append(i)     #"if" que nos permite fazer verificações na leitura
        map.append(map_lines)

#Função responsável por mostrar na tela a matriz
def display_matrix(): 
    for i in map:   #"For" simples para mostrar a matriz na tela
        print("".join(i))

#Função responsável por mostrar quanto dinheiro foi recuperado
def display_saved_money():
    print(money)

#Função responsável por encotrar onde se deve iniciar o caminhamento no mapa
def find_first_location():
    count = 0
    for i in map:         #"For" que percorre a primeira coluna da map até encontrar o inicio do mapa "-"
        if i[0] == "-":
            location = count
        count = count + 1 
    return location      #Retorna a coordenada em X(linha) do inicio do mapa 

#Função responsável por finalizar o programa
def end(coord_x, coord_y):
    if map[coord_x][coord_y] == "#": #Teste para saber se chegamos ao final do mapa 
        display_saved_money()
        exit()                              #Caso o teste seja verdadeiro, fecha o programa



#Funções de verificação para as trocas de direção
    
#Fumção responsável por testar se estamos caminhando por uma "\\"
#O que indica que devemos mudar a direção do caminhamento
def test_backslah(x,y):
    if map[x][y] == "\\":       #Teste para saber se chegamos em uma "quina" do mapa
        return True
    else:
        return False 

#Fumção responsável por testar se estamos caminhando por uma "/"
#O que indica que devemos mudar a direção do caminhamento
def test_slash(x,y):
    if map[x][y] == "/":        #Teste para saber se chegamos em uma "quina" do mapa
        return True
    else:
        return False



#Funções para caminnhar na matriz

#Função responsável por fazer o caminhamento para a direita na matriz         
def move_right(coord_x, coord_y):
    global money
    count = "0"

    print("andando pra direita")

    for i in range(coord_y, len(map[0])):  #Percorre a matriz para a direita apenas em Y(colunas)
        end(coord_x, i)                   
                                          
        if map[coord_x][i].isdigit():  
            count += map[coord_x][i]
        else:
            if count != "0":
                print(count)
            money += int(count)
            count = "0"

        if test_slash(coord_x,i):
            move_up(coord_x - 1, i)
            break
        if test_backslah(coord_x, i):
            move_down(coord_x + 1, i)
            break

#Função responsável por fazer o caminhamento para cima na matriz    
def move_up(coord_x, coord_y):
    global money
    count = "0"
    print("andando pra cima")
    
    for i in range(coord_x, 0, -1): #podemos otimizar
        end(i, coord_y)
            
        if map[i][coord_y].isdigit():
            count += map[i][coord_y]
        else:
            if count != "0":
                print(count)
            money += int(count)
            count = "0"

        if test_backslah(i, coord_y):
            move_left(i, coord_y - 1)
            break
        if test_slash(i, coord_y):
            move_right(i, coord_y + 1)
            break
        
#Função responsável por fazer o caminhamento para a esquerda na matriz           
def move_left(coord_x, coord_y):
    global money
    count ="0"
    print("andando pra esquerda")

    for i in range(coord_y, 0, -1):
        end(coord_x, i)
            
        if map[coord_x][i].isdigit():
            count += map[coord_x][i]
        else:
            if count != "0":
                print(count)
            money += int(count)
            count = "0"

        if test_backslah(coord_x, i):
            move_up(coord_x - 1, i)
            break
        if test_slash(coord_x, i):
            move_down(coord_x + 1, i)
            break
        
#Função responsável por fazer o caminhamento para baixo na matriz    
def move_down(coord_x, coord_y):
    global money
    count = "0"
    print("andando pra baixo")

    for i in range(coord_x, len(map[0])):
        end(i, coord_y)
            
        if map[i][coord_y].isdigit():
            count += (map[i][coord_y])
        else:
            if count != "0":
                print(count)
            money += int(count)
            count = "0"

        if test_backslah(i, coord_y):
            move_right(i, coord_y + 1)
            break
        if test_slash(i, coord_y):
            move_left(i, coord_y - 1)
            break



# Função Main()
def main():

    os.system("cls")

    read_map()
    display_matrix()
    
    first_location_x = find_first_location()
    first_location_y = 0

    move_right(first_location_x, first_location_y)
    print(money)
    
if __name__ == "__main__":
  main()