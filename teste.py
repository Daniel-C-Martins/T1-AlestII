import os

matriz = []

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


def troca_direcao(proximo_x, proximo_y):
    #Teste de troca posição
    if matriz[proximo_x][proximo_y] == "\\" or "/":
        return True
    else:
        return False
    
def anda_direita(localização):
    localização = matriz[x+1][y]

def main():
    os.system("cls")

    le_mapa()
    mostra_matriz()

    localizao_inicial = acha_primeira_localização()


    mudar_rota = troca_direcao(proximo_x, proximo_y)


    

    #Teste de posição válida
    #matriz[localização_inicio][0]
    # x = localização_inicio
    # y = 0
    
    # if matriz[x+1][y] != " ":
    #     proximo_x = x+1
    #     proximoo_y = y
    #     direcao = "direita"

    # if matriz[x-1][y]!= " ":
    #     proximo_x = x-1
    #     proximoo_y = y
    #     direcao = "esquerda"

    # if matriz[x][y+1]!= " ":
    #     proximo_x = x
    #     proximoo_y = y+1
    #     direcao = "baixo"

    # if matriz[x-1][y]!= " ":
    #     proximo_x = x
    #     proximoo_y = y-1
    #     direcao = "cima"

     
  

if __name__ == "__main__":
  main()
