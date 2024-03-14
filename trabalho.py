import os

#Variáveis globais importantes
matriz = []
acumulador = 0

#Funções de leitura do mapa

#Função responsável por ler o mapa.txt para uma matriz
def le_mapa():
    with open("Mapas\mapa50.txt", "r") as arquivo: #Leitura das linhas do arquivo txt para uma variável 
        arquivo_linhas = arquivo.readlines()
        
    for linha in arquivo_linhas:    #"For" responsável por colocar as linhas na matriz
        linhamatriz = []
        for i in linha:             
            if i != "\n":           #"if" que nos permite fazer verificações na leitura
                linhamatriz.append(i)
        matriz.append(linhamatriz)

#Função responsável por mostrar na tela a matriz
def mostra_matriz(): 
    for i in matriz:   #"For" simples para mostrar a matriz na tela
        print(i)

#Função responsável por encotrar onde se deve iniciar o caminhamento no mapa
def acha_primeira_localização():
    count = 0
    for i in matriz:         #"For" que percorre a primeira coluna da matriz até encontrar o inicio do mapa "-"
        if i[0] == "-":
            localização = count
        count = count + 1 
    return localização      #Retorna a coordenada em X(linha) do inicio do mapa 

#Função responsável por finalizar o programa
def fim(posicao_x, posicao_y):
    if matriz[posicao_x][posicao_y] == "#": #Teste para saber se chegamos ao final do mapa 
        exit()                              #Caso o teste seja verdadeiro, fecha o programa



#Funções de verificação para as trocas de direção
    
#Fumção responsável por testar se estamos caminhando por uma "\\"
#O que indica que devemos mudar a direção do caminhamento
def testa_barra_invertida(x,y):
    if matriz[x][y] == "\\":       #Teste para saber se chegamos em uma "quina" do mapa
        return True
    else:
        return False 

#Fumção responsável por testar se estamos caminhando por uma "/"
#O que indica que devemos mudar a direção do caminhamento
def testa_barra_normal(x,y):
    if matriz[x][y] == "/":        #Teste para saber se chegamos em uma "quina" do mapa
        return True
    else:
        return False



#Funções para caminnhar na matriz

#Função responsável por fazer o caminhamento para a direita na matriz           
def anda_direita(posicao_x, posicao_y):
    print("andando pra direita")

    for i in range(posicao_y, len(matriz[0])):  #Percorre a matriz para a direita apenas em Y(colunas)
        fim(posicao_x, i)                   
                                          
        if matriz[posicao_x][i].isdigit():  
            print(matriz[posicao_x][i])

        if testa_barra_normal(posicao_x,i):
            anda_cima(posicao_x - 1, i)
            break
        if testa_barra_invertida(posicao_x, i):
            anda_baixo(posicao_x + 1, i)
            break

#Função responsável por fazer o caminhamento para cima na matriz    
def anda_cima(posicao_x, posicao_y):
    print("andando pra cima")

    for i in range(posicao_x, 0, -1): #podemos otimizar
        fim(i, posicao_y)
            
        if matriz[i][posicao_y].isdigit():
            print(matriz[i][posicao_y])

        if testa_barra_invertida(i, posicao_y):
            anda_esquerda(i, posicao_y - 1)
            break
        if testa_barra_normal(i, posicao_y):
            anda_direita(i, posicao_y + 1)
            break
        
#Função responsável por fazer o caminhamento para a esquerda na matriz           
def anda_esquerda(posicao_x, posicao_y):
    print("andando pra esquerda")

    for i in range(posicao_y, 0, -1):
        fim(posicao_x, i)
            
        if matriz[posicao_x][i].isdigit():
            print(matriz[posicao_x][i])

        if testa_barra_invertida(posicao_x, i):
            anda_cima(posicao_x - 1, i)
            break
        if testa_barra_normal(posicao_x, i):
            anda_baixo(posicao_x + 1, i)
            break
        
#Função responsável por fazer o caminhamento para baixo na matriz    
def anda_baixo(posicao_x, posicao_y):
    print("andando pra baixo")

    for i in range(posicao_x, len(matriz[0])):
        fim(i, posicao_y)
            
        if matriz[i][posicao_y].isdigit():
            print(matriz[i][posicao_y])

        if testa_barra_invertida(i, posicao_y):
            anda_direita(i, posicao_y + 1)
            break
        if testa_barra_normal(i, posicao_y):
            anda_esquerda(i, posicao_y - 1)
            break


#Função responsável por garantir a contagem certa do dinheiro recuperado
# def conta_dinheiro(posicao_x, posicao_y):

#     for i in range (0, len(matriz[0])):
#         if matriz[posicao_x][posicao_y].isdigit():
#             acumulador_secundario = ac + matriz[posicao_x][posicao_y]
#         if testa_barra_invertida(posicao_x, posicao_y) or testa_barra_normal(posicao_x, posicao_y):
#             break
#         else:
#             if not matriz[posicao_x - 1][posicao_y].isdigit():  
#                 acumulador += int(b)   
#                 acumulador_secundario = ""

# Função Main()
def main():    
    os.system("cls")

    le_mapa()
    mostra_matriz()
    
    primeira_posicao_x = acha_primeira_localização()
    primeira_posicao_y = 0

    anda_direita(primeira_posicao_x, primeira_posicao_y)
    print(acumulador)
    
if __name__ == "__main__":
  main()
