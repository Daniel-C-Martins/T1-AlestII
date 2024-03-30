import matplotlib.pyplot as plt
import numpy as np

width = 0.2

maps = ["50", "100", "200", "500", "750", "1000", "1500", "2000"]
alg1 = [6_643, 25_957, 101_963, 629_079, 1_412_714, 2_509_607, 5_637_545, 10_019_131]
alg2 = [7_894, 30_981, 122_000, 754_090, 1_694_037, 3_009_916, 6_762_586, 12_019_712]
alg3 = [6_644, 25_958, 101_964, 629_080, 1_412_715, 2_509_608, 5_637_546, 10_019_132]

xposition = np.arange(len(maps))


plt.bar(xposition-width, alg1, width, label="alg1")
plt.bar(xposition, alg2, width, label="alg2")
plt.bar(xposition+width, alg3, width, label="alg3")

plt.xticks(xposition, maps)
plt.xlabel("Mapas")
plt.ylabel("Contagem de Operações")
plt.title("Comparação algoritmos - Contagem de operações")
plt.legend()
plt.show()

