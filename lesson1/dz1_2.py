'''
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
'''
a = 5
b = 6
print(bin(a))
print(bin(b))
## побитовое И
print(bin(a & b))
##побитовое ИЛИ
print(bin(a | b))
##побитовое XOR
print(bin(a ^ b))
##сдвиг влево
print(bin(a << 1))
##сдвиг вправо
print(bin(a >> 1))