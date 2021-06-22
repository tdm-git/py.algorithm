"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
# мне кажется можно развернуть условие задачи - т.е. оптимальнее будет не проверять на кратность а наоборот,
# для числе от 2 до 9 - используя функцию range() с кратным шагом складывать значения в отдельный список
result = []
for i in range(2, 10):  # от 2 до 9
    for j in range(i, 100, i):  # от 2..9 до 99
        result.append(j)
# ответом на вопрос задачи  тогда будет длина этого списка
# print(result)
print('в диапазоне 2-99 - количество чисел кратных числам из диапазона 2-9 : ', len(result))

# или этот же вариант решения в одну строку
res = [j for i in range(2, 10) for j in range(i, 100, i)]
# print(res)
print('в диапазоне 2-99 - количество чисел кратных числам из диапазона 2-9 : ', len(res))
