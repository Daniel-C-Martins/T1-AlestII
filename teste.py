import os
a = [[50], [50]];


def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        primeira_linha = arquivo.readline()
        tamanho_matriz = primeira_linha[:2]
        
        a = [[tamanho_matriz],[tamanho_matriz]]

        
    # for linha in arquivo:
    #   exit()     

if __name__ == "__main__":
  main()