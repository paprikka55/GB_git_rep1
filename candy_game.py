import random
player1 = 0   #Первый игрок
player2 = 0   #Второй игрок
random_num = 0
bank = int(input("Введите сумму банка (любое целое число): "))   #Банк
random_num = random.randint(0, 1)
if random_num == 0:         #Определяем кто первый ходит
  last_player1 = True
else: 
  last_player1 = False
while bank > 0:
  random_num = random.randint(0, 28)
  if random_num < bank:
    if last_player1 == True:
      player2 = player2 + random_num
      bank = bank - random_num
      last_player1 = False
    else:
      player1 = player1 + random_num
      bank = bank - random_num
      last_player1 = True
  else:
    if last_player1 == True:
      player2 = player2 + bank
      bank = bank - random_num
    else:
      player1 = player1 + bank
      bank = bank - random_num
summ = player1 + player2
if player1 > player2:
  print('Победил игрок 1, со счетом: ' + str(player1) + ' конфет! ' + 'Конфеты игрока номер 2: ' + str(player2) + ' достаются игроку номер 1! Итого у игрока номер 1: ' + str(summ) + ' конфет!')
else:
  print('Победил игрок 2, со счетом: ' + str(player2) + ' конфет! ' + 'Конфеты игрока номер 1: ' + str(player1) + ' достаются игроку номер 2! Итого у игрока номер 2: ' + str(summ) + ' конфет!')