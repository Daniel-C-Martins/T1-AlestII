import os, sys
from time import process_time


# File usada para análise assintótica das funções
# Para contagem de operações e geração de gráficos


map = []
location_x = 0
location_y = 0

way = "right" 
end_controller = False

money = 0
count = "0"

count_op = 0


def read_map(chosen_map):
    global count_op
    count_op += 1
    with open("Maps\\" + chosen_map +".txt", "r") as archive: 
        archive_lines = archive.readlines()
    # Θ(n2) Os dois laços de repetição da função crescem em relação a N (Tamanho do mapa)    
    for lines in archive_lines:         
        map_lines = []
        for i in lines:                           
            if i != "\n":
                map_lines.append(i)     
        map.append(map_lines)       


def display_matrix():
    global count_op
    count_op += 1
    # Θ(n) O laço de repetição cresce de acordo com o tamanho de N (Tamanho do mapa)  
    for line in map:   
        print("".join(line))


def find_first_location():
    global count_op
    count_op += 1
    count = 0
    # O(n) Será necessário percorrer o tamanho do mapa para achar o inicio
    # Ω(1) O mapa inicia na primeira linha da primeira coluna
    for i in map:         
        if i[0] == "-":
            location = count
        count = count + 1 
    return location       



#Funções de verificação para as trocas de direção    
def test_backslah(x,y):
    global count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    if map[x][y] == "\\":       
        return True
    else:
        return False 


def test_slash(x,y):
    global count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    if map[x][y] == "/":        
        return True
    else:
        return False



#Funções para caminhar na matriz        
def move_right(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    accumulate_money(coord_x, coord_y)    

    if end(coord_x, coord_y):         
        end_controller = True   
        return
    if test_slash(coord_x, coord_y): 
        way = "up"  
        location_x = coord_x - 1
        location_y = coord_y  
        return
    if test_backslah(coord_x, coord_y): 
        way = "down"  
        location_x = coord_x + 1
        location_y = coord_y  
        return
      
    move_right(coord_x, coord_y + 1)
  
         
def move_left(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    accumulate_money(coord_x, coord_y)    

    if end(coord_x, coord_y):         
        end_controller = True   
        return
    
    if test_slash(coord_x, coord_y): 
        way = "down"  
        location_x = coord_x + 1
        location_y = coord_y  
        return
        
    if test_backslah(coord_x, coord_y): 
        way = "up"  
        location_x = coord_x - 1
        location_y = coord_y  
        return
      
    move_left(coord_x, coord_y - 1)
           
                              
def move_up(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    accumulate_money(coord_x, coord_y)    

    if end(coord_x, coord_y):         
        end_controller = True   
        return
    if test_slash(coord_x, coord_y): 
        way = "right"  
        location_x = coord_x
        location_y = coord_y + 1    
        return
    if test_backslah(coord_x, coord_y): 
        way = "left"  
        location_x = coord_x
        location_y = coord_y - 1    
        return
    
    move_up(coord_x - 1, coord_y)
        
          
def move_down(coord_x, coord_y):
    global way, money, end_controller, location_x, location_y, count, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    accumulate_money(coord_x, coord_y)    

    if end(coord_x, coord_y):         
        end_controller = True   
        return
    
    if test_slash(coord_x, coord_y): 
        way = "left"  
        location_x = coord_x
        location_y = coord_y - 1    
        return

    if test_backslah(coord_x, coord_y): 
        way = "right"  
        location_x = coord_x
        location_y = coord_y + 1    
        return
    
    move_down(coord_x + 1, coord_y)
      
#Funções relacionadas com dinheiro
def display_saved_money():
    global money, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    thousandion = 0  
    hundred_thousand = 0
    ten_thousand = 0
    thousand = 0
    hundred = 0
    ten = 0
    one = 0
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

    print("O total recuperado pela polícia no mapa foi:")
    print("R$ " + str(thousandion) + "."+ str(hundred_thousand) + str(ten_thousand) + str(thousand) + "." + str(hundred) +str(ten) + str(one))


def accumulate_money(coord_x, coord_y):
    global count, money, count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    if map[coord_x][coord_y].isdigit():
        count += map[coord_x][coord_y]  
    else:
        money += int(count) 
        count = "0" 



#Funções gerais do programa
def menu():
    global count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso 
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


def start():
    global count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    option = 0
    user_input = input(menu())  

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
    
    if user_input.isdigit():   
        option = switcher.get(int(user_input))
    if option:  
        return option
    else:
        print("Opção inválida")
        return start()  


def end(coord_x, coord_y):
    global count_op
    count_op += 1
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    if map[coord_x][coord_y] == "#": 
        return True
    else:
        return False
    

def controller():
    global way, end_controller, location_x, location_y, count_op
    location_x = find_first_location()  
    #Ω(1) o fim do mapa está logo no começo
    #O(n) O fim do mapa está qualquer outra posição e será necessário percorrer para achar ele
    
    while(end_controller == False): 
      if way == "right":
        count_op += 1
        move_right(location_x, location_y)  
      if way == "left":
        count_op += 1
        move_left(location_x, location_y)   
      if way == "up":
        count_op += 1
        move_up(location_x, location_y) 
      if way == "down":
        count_op += 1
        move_down(location_x, location_y)  



# Função Main()
def main():
    global count_op
    sys.setrecursionlimit(2000)
    #Θ(1) A Função inteira possui a complexidade constante no melhor e no pior caso
    os.system("cls") 
    chosen_map = start()
    start_time = process_time()
    read_map(chosen_map) 
    #display_matrix() 
    controller() 
    display_saved_money()
    end_time = process_time()
    time = end_time-start_time
    print(f"Tempo para ordenar o mapa {chosen_map}: {time} s")
    print(f"Acontecer {count_op} operações no mapa {chosen_map}")
    exit() 
    
if __name__ == "__main__":
  main()