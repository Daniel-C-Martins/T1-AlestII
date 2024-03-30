import matplotlib.pyplot as plt

width = 0.2

maps = ["50", "100", "200", "500", "750", "1000", "1500", "2000"]
alg1 = [0.000, 0.000, 0.031, 0.187, 0.406, 0.640, 1.703, 2.734]
alg2 = [0.000, 0.000, 0.046, 0.265, 0.546, 0.796, 2.562, 3.375]
alg3 = [0.000, 0.000, 0.053, 0.246, 0.500, 0.701, 1.810, 2.920]

'''xposition = np.arange(len(maps))


plt.bar(xposition-width, alg1, width, label="alg1")
plt.bar(xposition, alg2, width, label="alg2")
plt.bar(xposition+width, alg3, width, label="alg3")

plt.xticks(xposition, maps)'''
plt.plot(maps, alg1, label="alg1")
plt.plot(maps, alg2, label="alg2")
plt.plot(maps, alg3, label="alg3")
plt.xlabel("Mapas")
plt.ylabel("Tempo (s)")
plt.title("Comparação algoritmos - Tempo de Execução")
plt.legend()
plt.show()

