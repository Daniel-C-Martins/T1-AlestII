import os

#Variáveis globais do mapa
map = []
location_x = 0
location_y = 0

#Variáveis globais de direção e controle 
way = "right"
end_controller = False

#Variável globais relacionadas com dinheiro
money = 0
count = "0"

#Funções de leitura do mapa
#Função responsável por ler o mapa.txt para uma matriz
def read_map():
    with open("Maps\map100.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
        archive_lines = archive.readlines()
        
    for lines in archive_lines:         #"For" responsável por ler cada linha
        map_lines = []
        for i in lines:                 #"For" responsável por ler cada caracter da linha para a lista             
            if i != "\n":
                map_lines.append(i)     #"if" que nos permite fazer verificações na leitura
        map.append(map_lines)       #Adiciona cada lista no mapa como uma linha

#Função responsável por mostrar na tela o mapa
def display_matrix(): 
    for line in map:   #"For" simples para mostrar o mapa na tela
        print("".join(line))

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
#Função responsável por fazer o caminhamento para a right na matriz         
def move_right(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    for i in range(coord_y, len(map[1]) + 1):   #Percorre o mapa para a direita apenas em Y(colunas)
        if end(coord_x, i):         #Chama o método responsável por testar se chegamos no "#""
            end_controller = True   #Muda o controlador para True e volta para o loop inicial
            break

        accumulate_money(coord_x, i)    #Chama o método responsável por contar o dinheiro recuperado

        if test_slash(coord_x,i): #Chama o método responsável para saber se estamos passando por uma "/"
            way = "up"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = coord_x - 1
            location_y = i  #Atualiza a localização em X e em Y
            break
        if test_backslah(coord_x, i): #Chama o método responsável para saber se estamos passando por uma "\"
            way = "down"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = coord_x + 1
            location_y = i  #Atualiza a localização em X e em Y
            break
  
#Função responsável por fazer o caminhamento para a left na matriz           
def move_left(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    for i in range(coord_y, -1, -1):    #Percorre o mapa para a esquerda apenas em Y(colunas)   
        if end(coord_x, i):         #Chama o método responsável por testar se chegamos no "#""
            end_controller = True   #Muda o controlador para True e volta para o loop inicial
            break

        accumulate_money(coord_x, i)    #Chama o método responsável por contar o dinheiro recuperado

        if test_slash(coord_x, i): #Chama o método responsável para saber se estamos passando por uma "/"
            way = "down"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = coord_x + 1
            location_y = i  #Atualiza a localização em X e em Y
            break
        if test_backslah(coord_x, i): #Chama o método responsável para saber se estamos passando por uma "\"
            way = "up"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = coord_x - 1
            location_y = i  #Atualiza a localização em X e em Y
            break 
                           
#Função responsável por fazer o caminhamento para up na matriz    
def move_up(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count
    
    for i in range(coord_x, -1, -1):    #Percorre o mapa para cima apenas em X(linhas) 
        if end(i, coord_y):         #Chama o método responsável por testar se chegamos no "#""
            end_controller = True   #Muda o controlador para True e volta para o loop inicial
            break

        accumulate_money(i, coord_y)    #Chama o método responsável por contar o dinheiro recuperado
        
        if test_slash(i, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
            way = "right"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = i
            location_y = coord_y + 1    #Atualiza a localização em X e em Y
            break
        if test_backslah(i, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
            way = "left"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = i
            location_y = coord_y - 1    #Atualiza a localização em X e em Y
            break
        

        
#Função responsável por fazer o caminhamento para down na matriz    
def move_down(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    for i in range(coord_x, len(map) + 1):  #Percorre o mapa para baixo apenas em X(linhas) 
        if end(i, coord_y):         #Chama o método responsável por testar se chegamos no "#""
            end_controller = True   #Muda o controlador para True e volta para o loop inicial
            break

        accumulate_money(i, coord_y)    #Chama o método responsável por contar o dinheiro recuperado
        
        if test_slash(i, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
            way = "left"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = i
            location_y = coord_y - 1    #Atualiza a localização em X e em Y
            break
        if test_backslah(i, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
            way = "right"  #Faz a troca para a nova direção correta na variável de controle de direção
            location_x = i
            location_y = coord_y + 1    #Atualiza a localização em X e em Y
            break
        


#Funções relacionadas com dinheiro
#Função responsável por mostrar quanto dinheiro foi recuperado
def display_saved_money():
    print(money)

#Função responsável acumular o dinheiro recolhido
def accumulate_money(coord_x, coord_y):
    global count, money
    if map[coord_x][coord_y].isdigit(): #Testa se a posição que estamos é um número
        count += map[coord_x][coord_y]  #Concatena no acumulador o número
    else:
        money += int(count) #Converte o acumulador para inteiro e guarda na variável do dinheiro
        count = "0" #Reset no acumulador

# Função Main()
def main():
    global way, end_controller, location_x, location_y
    os.system("cls")

    read_map()
    #display_matrix()
    
    location_x = find_first_location()

    while(end_controller == False):
      if way == "right":
        move_right(location_x, location_y)
      if way == "left":
        move_left(location_x, location_y)
      if way == "up":
        move_up(location_x, location_y)
      if way == "down":
        move_down(location_x, location_y) 

    print("Caminhamento concluido")
    display_saved_money()
    exit()
    
if __name__ == "__main__":
  main()