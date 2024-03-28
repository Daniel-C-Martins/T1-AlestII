import os

#Variáveis globais do mapa
map = []
location_x = 0
location_y = 0

#Variáveis globais de direção e controle 
way = "right" #inicializado como "right", pois, o mapa sempre começa indo para a direita
end_controller = False

#Variável globais relacionadas com dinheiro
money = 0
count = "0"

#Funções de leitura do mapa
#Função responsável por ler o mapa.txt para uma matriz
def read_map(chosen_map):
    with open("Maps\\" + chosen_map +".txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
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



#Funções para caminhar na matriz
#Função responsável por fazer o caminhamento para a direita na matriz         
def move_right(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    accumulate_money(coord_x, coord_y)    #Chama o método responsável por contar o dinheiro recuperado

    if end(coord_x, coord_y):         #Chama o método responsável por testar se chegamos no "#""
        end_controller = True   #Muda o controlador para True e volta para o loop inicial
        return
    else:
      if test_slash(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
          way = "up"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x - 1
          location_y = coord_y  #Atualiza a localização em X e em Y
          return

      if test_backslah(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
          way = "down"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x + 1
          location_y = coord_y  #Atualiza a localização em X e em Y
          return
      
      location_x = coord_x
      location_y = coord_y + 1
  

#Função responsável por fazer o caminhamento para a esquerda na matriz           
def move_left(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    accumulate_money(coord_x, coord_y)    #Chama o método responsável por contar o dinheiro recuperado

    if end(coord_x, coord_y):         #Chama o método responsável por testar se chegamos no "#""
        end_controller = True   #Muda o controlador para True e volta para o loop inicial
        return
    else:
      if test_slash(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
          way = "down"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x + 1
          location_y = coord_y  #Atualiza a localização em X e em Y
          return
        
      if test_backslah(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
          way = "up"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x - 1
          location_y = coord_y  #Atualiza a localização em X e em Y
          return
      
      location_x = coord_x
      location_y = coord_y - 1
           
                           
#Função responsável por fazer o caminhamento para cima na matriz    
def move_up(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count
    
    accumulate_money(coord_x, coord_y)    #Chama o método responsável por contar o dinheiro recuperado

    if end(coord_x, coord_y):         #Chama o método responsável por testar se chegamos no "#""
        end_controller = True   #Muda o controlador para True e volta para o loop inicial
        return
    else:
      if test_slash(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
          way = "right"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x
          location_y = coord_y + 1    #Atualiza a localização em X e em Y
          return

      if test_backslah(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
          way = "left"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x
          location_y = coord_y - 1    #Atualiza a localização em X e em Y
          return
      location_x = coord_x - 1
      location_y = coord_y
        

        
#Função responsável por fazer o caminhamento para baixo na matriz    
def move_down(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count

    accumulate_money(coord_x, coord_y)    #Chama o método responsável por contar o dinheiro recuperado

    if end(coord_x, coord_y):         #Chama o método responsável por testar se chegamos no "#""
        end_controller = True   #Muda o controlador para True e volta para o loop inicial
        return
    else:
      if test_slash(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "/"
          way = "left"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x
          location_y = coord_y - 1    #Atualiza a localização em X e em Y
          return

      if test_backslah(coord_x, coord_y): #Chama o método responsável para saber se estamos passando por uma "\"
          way = "right"  #Faz a troca para a nova direção correta na variável de controle de direção
          location_x = coord_x
          location_y = coord_y + 1    #Atualiza a localização em X e em Y
          return
    
      location_x = coord_x + 1
      location_y = coord_y
        


#Funções relacionadas com dinheiro
#Função responsável por mostrar quanto dinheiro foi recuperado
def display_saved_money():
    global money
    thousandion = 0  
    hundred_thousand = 0
    ten_thousand = 0
    thousand = 0
    hundred = 0
    ten = 0
    one = 0

    #Esquema padrão para descobrir a quantidade de cada unidade de medida do valor total
    aux = money
    if aux >= 1000000:
        thousandion = aux // 1000000
        aux = aux % 1000000
    if aux >= 100000:
        hundred_thousand = aux // 100000
        aux = aux % 100000
    if aux >= 10000:
        ten_thousand = aux // 10000
        aux = aux % 10000
    if aux >= 1000:
        thousand = aux // 1000
        aux = aux % 1000
    if aux >= 100:
        hundred = aux // 100
        aux = aux % 100
    if aux >= 10:
        ten = aux // 10
        aux = aux % 10
    if aux >= 1:
        one = aux // 1
        aux = 0

    #Print formatado para acomodar até centenas de milhões como unidade de medida 
    print("O total recuperado pela polícia no mapa foi:")
    print("R$ " + str(thousandion) + "."+ str(hundred_thousand) + str(ten_thousand) + str(thousand) + "." + str(hundred) + str(ten) + str(one))

#Função responsável acumular o dinheiro recolhido
def accumulate_money(coord_x, coord_y):
    global count, money
    if map[coord_x][coord_y].isdigit(): #Testa se a posição que estamos é um número
        count += map[coord_x][coord_y]  #Concatena no acumulador o número
    else:
        money += int(count) #Converte o acumulador para inteiro e guarda na variável do dinheiro
        count = "0" #Reset no acumulador



#Funções gerais do programa
#Função responsável pelo menu de opções
def menu():
    text = """
    ==========================================
    Escolha a opção de mapa que deseja testar:
    ==========================================
    1. Mapa 50x50
    2. Mapa 100x100
    3. Mapa 200x200
    4. Mapa 500x500
    5. Mapa 750x750
    6. Mapa 1000x1000
    7. Mapa 1500x1500
    8. Mapa 2000x2000 
    """
    return text

#função responsável por dar ao usuário a possibilidade de escolher o mapa que deseja percorrer
def start():
    option = 0
    user_input = input(menu())  #Recebe a opção do usuário

    switcher = {
        1: "map50",
        2: "map100",
        3: "map200",
        4: "map500",
        5: "map750",
        6: "map1000",
        7: "map1500",
        8: "map2000"
    }
    
    if user_input.isdigit():    #Teste para saber se o usuário digitou um número
        option = switcher.get(int(user_input))
    if option:  #Teste para saber se o número digitado é válido
        return option
    else:
        print("Opção inválida")
        return start()  #Chama recursivamente novamente o método caso o número seja inválido

#Função responsável por finalizar o programa
def end(coord_x, coord_y):
    if map[coord_x][coord_y] == "#": #Teste para saber se chegamos ao final do mapa
        return True
    else:
        return False
    
#Função responsável pelo loop que controla o caminhamento e o fim do código
def controller():
    global way, end_controller, location_x, location_y
    location_x = find_first_location()  #Recebe a posição do início do mapa

    while(end_controller == False): #Loop que controla o caminhamento pelo mapa
      if way == "right":
        move_right(location_x, location_y)  #Chama o caminhamento para a direita
      if way == "left":
        move_left(location_x, location_y)   #Chama o caminhamento para a esquerda
      if way == "up":
        move_up(location_x, location_y) #Chama o caminhamento para cima
      if way == "down":
        move_down(location_x, location_y)   #Chama o caminhamento para baixo



# Função Main()
def main():
    os.system("cls") 
    chosen_map = start()
    read_map(chosen_map)  #Lê o mapa e "Começa" o código
    #display_matrix() #Mostra o mapa na tela
    controller() #Chama o método que controla o caminhamento
    display_saved_money() #Mostra o total de dinheiro recolhido na tela
    exit() #Fecha o programa após o fim da execução
    
if __name__ == "__main__":
  main()