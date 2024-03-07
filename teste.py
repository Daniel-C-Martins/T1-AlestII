import os


def main():
    os.system("cls")

    with open("Mapas\mapa50.txt", "r") as arquivo:
        
<<<<<<< HEAD
=======
        matriz = [[tamanho_matriz_x],[tamanho_matriz_y]]

        
    for linha in arquivo_linhas:
        linhamatriz = []
        for i in linha:
            if i != "\n":

                linhamatriz.append(i)
        matriz.append(linhamatriz)
>>>>>>> 5fa934cba1d4cdbff64b0896c66e09dd2c76e238
           
    for i in matriz:
        print(i)

if __name__ == "__main__":
  main()
