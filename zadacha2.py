mas1 = [19, 2, 37, 4, 52, 6, 7, 8, 9]
mas2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
mas3 = [i for i in mas1 if i not in mas2]
print(mas1, mas2, mas3)