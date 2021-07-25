#N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, кто кому и сколько должен, и они придумали
#систему долговых расписок. И чтобы начать новый год «с чистого листа», друзья решили оплатить все долговые расписки, которые накопились
#у них друг к другу. Однако выяснилось, что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.

#Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый друг выплатить другим (или получить с других).

#Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок, после этого следует K троек чисел:
#номер друга, взявшего в долг, номер друга, давшего деньги, и сумма. Гарантируется, что ни один друг не брал в долг сам у себя.
#Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья. Положительное число означает,
#что друг должен получить деньги от других, отрицательное — должен отдать деньги.

#Пример 1:
#Кол-во друзей: 2
#Долговых расписок: 3

#1 расписка
#Кому: 1
#От кого: 2
#Сколько: 10

#2 расписка
#Кому: 1
#От кого: 2
#Сколько: 20

#3 расписка
#Кому: 1
#От кого: 2
#Сколько: 20

#Баланс друзей:
#1 : -50
#2 : 50

#Пример 2:
#Кол-во друзей: 3
#Долговых расписок: 1

#1 расписка
#Кому: 3
#От кого: 1
#Сколько: 100

#Баланс друзей:
#1 : 100
#2 : 0
#3 : -100

debt_lst = []
for i in range(int(input('Кол-во друзей: '))):
    debt_lst.append([i+1, 0])
cnt_rec = int(input('Долговых расписок: '))

for i in range(cnt_rec):
    print('\n', i+1, 'расписка')
    lender = int(input('Кому: '))
    debtor = int(input('От кого: '))
    while debtor == lender: debtor = int(input('От кого: '))
    summ = int(input('Сколько: '))
    debt_lst[debtor-1][1] -= summ
    debt_lst[lender-1][1] += summ

print('\nБаланс друзей:')
for i in range(len(debt_lst)):
    print(i+1, ':', debt_lst[i][1])