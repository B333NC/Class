#Ввести 2 массива из 16 и 12 эл-тов, созд. третий массив из эл-тов, которые входят в оба массива
mas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
mas2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
mas3 = [i for i in mas1 if i in mas2]
print(mas1, mas2, mas3)