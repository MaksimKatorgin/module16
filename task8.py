#N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание, где каждый K-й по счёту
#человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
#На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер человека, который
#останется в кругу последним.

#Пример:
#Кол-во человек: 5
#Какое число в считалке? 7
#Значит, выбывает каждый 7 человек

#Текущий круг людей: [1, 2, 3, 4, 5]
#Начало счёта с номера 1
#Выбывает человек под номером 2

#Текущий круг людей: [1, 3, 4, 5]
#Начало счёта с номера 3
#Выбывает человек под номером 5

#Текущий круг людей: [1, 3, 4]
#Начало счёта с номера 1
#Выбывает человек под номером 1

#Текущий круг людей: [3, 4]
#Начало счёта с номера 3
#Выбывает человек под номером 3

#Остался человек под номером 4

def the_reader(participants, num_reader):
    for _ in range(len(participants)):
        number_of_participants = len(participants)
        if num_reader % number_of_participants == 0:
            index_deleted = (num_reader % number_of_participants)
            func_print(participants, index_deleted)
            del participants[index_deleted - 1]
            stop_game = len(participants)
            if stop_game == 1:
                print(f'\nОстался человек под номером { participants[0] } ')
                return
        else:
            index_deleted = (num_reader % number_of_participants)
            func_print(participants, index_deleted)
            del participants[index_deleted - 1]
            participants = participants[index_deleted - 1:] + participants[:index_deleted - 1]
            stop_game = len(participants)
            if stop_game == 1:
                print(f'\nОстался человек под номером { participants[0] } ')
                return

def func_print(participants, index_deleted):
    print(f'\nТекущий круг людей: { sorted(participants) } \nНачало счета с номера { participants[0] } \nВыбывает человек под '
f'номером { participants[index_deleted - 1] } ')

count_participants = int(input('Кол-во человек: '))
participants = list(range(1, count_participants + 1))
num_reader = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num_reader, 'человек')

the_reader(participants, num_reader)


