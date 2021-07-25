#Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
#Например, следующие последовательности являются симметричными:

#1 2 3 4 5 4 3 2 1

#1 2 1 2 2 1 2 1

#Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.

#Пример 1:
#Кол-во чисел: 5
#Число: 1
#Число: 2
#Число: 1
#Число: 2
#Число: 2

#Последовательность: 1 2 1 2 2
#Нужно приписать чисел: 3
#Сами числа: 1 2 1

#Пример 2:
#Кол-во чисел: 5
#Число: 1
#Число: 2
#Число: 3
#Число: 4
#Число: 5

#Последовательность: 1 2 3 4 5
#Нужно приписать чисел: 4
#Сами числа: 4 3 2 1

lst, lst_add = [], []
count = int(input('Кол-во чисел: '))
cnt_add = 0

for _ in range(count):
    lst.append(int(input('Число: ')))
print('\nПоследовательность:', end=' ')
for i in lst: print(i, end=' ')
print()
while True:
    part_1, part_2 = [], []
    cntr = len(lst) // 2 + len(lst) % 2
    for i in range(cntr):
        part_1.append(lst[i])
        part_2.append(lst[-(i+1)])
    if part_1 != part_2:
        lst_add.insert(0, lst[0])
        lst.pop(0)
        cnt_add += 1
    else:
        break

print('Нужно приписать чисел:', cnt_add)
print('Сами числа:', end=' ')
for i in lst_add: print(i, end=' ')