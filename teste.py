import os
a = [[50], [50]];


def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        primeira_linha = arquivo.readline()
        tamanho_matriz = primeira_linha[:2]
        
        matriz = [[tamanho_matriz],[tamanho_matriz]]
    
    for linha in linhas:
        teste = linha
        matriz.append([testado for testado in teste])
           
    for i in matriz:
        print(i)

if __name__ == "__main__":
  main()
