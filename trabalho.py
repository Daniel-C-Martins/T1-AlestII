import os

matriz = []
acumulador = 0
list = []

def le_mapa():
    #Leitura do mapa para a matriz
    with open("Mapas\mapa50.txt", "r") as arquivo:
        arquivo_linhas = arquivo.readlines()
        
    for linha in arquivo_linhas:
        linhamatriz = []
        for i in linha:
            if i != "\n":
                linhamatriz.append(i)
        matriz.append(linhamatriz)

def mostra_matriz():
    #Print da matriz 
    for i in matriz:   #Jeito simples de mostrar a matriz
        print(i)

def acha_primeira_localização():
    #Acha a localização do inicio
    count = 0
    for i in matriz: 
        if i[0] == "-":
            localização = count
        count = count + 1 

    return localização

def fim(posicao_x, posicao_y):
    if matriz[posicao_x][posicao_y] == "#":
        return True
    else:
        return False


#métodos de troca de direção
def testa_barra_invertida(x,y):
    if matriz[x][y] == "\\":
        return True
    else:
        return False 

def testa_barra_normal(x,y):
    if matriz[x][y] == "/":
        return True
    else:
        return False



#métodos para andar na matriz   
def anda_direita(posicao_x, posicao_y):
    print("andando pra direita")

    for i in range(posicao_y, len(matriz[0])): 
        if fim(posicao_x, i):
            exit()
        if matriz[posicao_x][i].isdigit():
            print(matriz[posicao_x][i])

        if testa_barra_normal(posicao_x,i):
            anda_cima(posicao_x - 1, i)
            break
        if testa_barra_invertida(posicao_x, i):
            anda_baixo(posicao_x + 1, i)
            break
   

def anda_cima(posicao_x, posicao_y):
    print("andando pra cima")

    for i in range(posicao_x, 0, -1): #podemos otimizar
        if fim(i, posicao_y):
            exit()
        if matriz[i][posicao_y].isdigit():
            print(matriz[i][posicao_y])

        if testa_barra_invertida(i, posicao_y):
            anda_esquerda(i, posicao_y - 1)
            break
        if testa_barra_normal(i, posicao_y):
            anda_direita(i, posicao_y + 1)
            break
        
        
def anda_esquerda(posicao_x, posicao_y):
    print("andando pra esquerda")
    for i in range(posicao_y, 0, -1):
        if fim(posicao_x, i):
            exit()
        if matriz[posicao_x][i].isdigit():
            print(matriz[posicao_x][i])

        if testa_barra_invertida(posicao_x, i):
            anda_cima(posicao_x - 1, i)
            break
        if testa_barra_normal(posicao_x, i):
            anda_baixo(posicao_x + 1, i)
            break
        
        
def anda_baixo(posicao_x, posicao_y):
    print("andando pra baixo")
    for i in range(posicao_x, len(matriz[0])):
        if fim(i, posicao_y):
            exit()
        if matriz[i][posicao_y].isdigit():
            print(matriz[i][posicao_y])

        if testa_barra_invertida(i, posicao_y):
            anda_direita(i, posicao_y + 1)
            break
        if testa_barra_normal(i, posicao_y):
            anda_esquerda(i, posicao_y - 1)
            break
            

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
