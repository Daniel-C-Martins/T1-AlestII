import os


def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        x = linhas[0][0 : 2]
        y = linhas[0][3 : 5]
        
        
    matriz = [[x],[y]]
    

    count = 0

    for linha in linhas:
        linhamatriz = []
        for i in linha:
            if i != "\n":
            
                linhamatriz.append(i)
        matriz.append(linhamatriz)
           
    for i in matriz:
        print(i)

if __name__ == "__main__":
  main()
