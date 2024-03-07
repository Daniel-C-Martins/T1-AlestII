import os

def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        arquivo_linhas = arquivo.readlines()
        primeira_linha = arquivo.readline()
        tamanho_matriz_x = primeira_linha[0 : 2]
        tamanho_matriz_z = primeira_linha[3 : 5]
        
        matriz = [[tamanho_matriz_x],[tamanho_matriz_z]]

        
    for linha in arquivo_linhas:
        linhamatriz = []
        for i in linha:
            if i != "\n":

                linhamatriz.append(i)
        matriz.append(linhamatriz)
           
    for i in matriz:
        print(i)

if __name__ == "__main__":
  main()
