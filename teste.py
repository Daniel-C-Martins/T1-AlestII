import os

def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        arquivo_linhas = arquivo.readlines()
        primeira_linha = arquivo.readline()
        tamanho_matriz_x = primeira_linha[0 : 2]
        tamanho_matriz_y = primeira_linha[3 : 5]
        
        matriz = [[tamanho_matriz_x],[tamanho_matriz_y]]

        
    for linha in arquivo_linhas:
        conteudo = linha
        matriz.append([caractere for caractere in conteudo])
           
    for i in matriz:
        print(i)

if __name__ == "__main__":
  main()
