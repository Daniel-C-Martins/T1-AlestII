import os

#Variáveis globais importantes
map = []
money = 0
direcao = "direita"
termina = False
location_x = 0
location_y = 0

#Funções de leitura do mapa

#Função responsável por ler o mapa.txt para uma matriz
def read_map():
    with open("Maps\ex.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
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
        return True
    else:
        return False



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
    global direcao, money, termina, location_x, location_y
    count = "0"
    print("andando direita")

    for i in range(coord_y, len(map[0])-1):  #Percorre a matriz para a direita apenas em Y(colunas)

      if end(coord_x, i):
          termina = True
          break

      if map[coord_x][i].isdigit():  
          count += map[coord_x][i]
      else:
          money += int(count)
          count = "0"
      
      if test_slash(coord_x,i):
          direcao = "cima"
          location_x = coord_x - 1
          location_y = i
          break
      if test_backslah(coord_x, i):
          direcao = "baixo"
          location_x = coord_x + 1
          location_y = i
          break
  
 #Função responsável por fazer o caminhamento para a esquerda na matriz           
def move_left(coord_x, coord_y):
    global direcao, money, termina, location_x, location_y
    count ="0"
    print("andando esquerda")

    for i in range(coord_y, -1, -1):
            
        if end(coord_x, i):
            termina = True
            break
        
        if map[coord_x][i].isdigit():
            count += map[coord_x][i]
        else:
            money += int(count)
            count = "0"

        
        if test_backslah(coord_x, i):
            direcao = "cima"
            location_x = coord_x - 1
            location_y = i
            break
        if test_slash(coord_x, i):
            direcao = "baixo"
            location_x = coord_x + 1
            location_y = i
            break 
                           
#Função responsável por fazer o caminhamento para cima na matriz    
def move_up(coord_x, coord_y):
    global direcao, money, termina, location_x, location_y
    count = "0"
    print("andando cima")
    
    for i in range(coord_x, -1, -1): 
        if end(i, coord_y):
          termina = True
          break

        if map[i][coord_y].isdigit():
            count += map[i][coord_y]
        else:
            money += int(count)
            count = "0"
        
        if test_slash(i, coord_y):
          direcao = "direita"
          location_x = i
          location_y = coord_y + 1
          break
        if test_backslah(i, coord_y):
          direcao = "esquerda"
          location_x = i
          location_y = coord_y - 1
          break
        

        
#Função responsável por fazer o caminhamento para baixo na matriz    
def move_down(coord_x, coord_y):
    global direcao, money, termina, location_x, location_y
    count = "0"
    print("andando baixo")

    for i in range(coord_x, len(map[0])-1):
        
        if end(i, coord_y):
            termina = True
            break

        if map[i][coord_y].isdigit():
            count += (map[i][coord_y])
        else:
            money += int(count)
            count = "0"

        
        if test_slash(i, coord_y):
            direcao = "esquerda"
            location_x = i
            location_y = coord_y - 1
            break
        if test_backslah(i, coord_y):
            direcao = "direita"
            location_x = i
            location_y = coord_y + 1
            break
        



# Função Main()
def main():
    global direcao, termina, location_x, location_y
    os.system("cls")

    read_map()
    #display_matrix()
    
    location_x = find_first_location()
    location_y = 0

    while(termina == False):
      if direcao == "direita":
        move_right(location_x, location_y)
      if direcao == "esquerda":
        move_left(location_x, location_y)
      if direcao == "cima":
        move_up(location_x, location_y)
      if direcao == "baixo":
        move_down(location_x, location_y) 

    print("Caminhamento concluido")
    display_saved_money()
    exit()
    
if __name__ == "__main__":
  main()