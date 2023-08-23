import random

print('''
      Добро пожаловать в чиловую угадайку
      Я загадаю число, а ты будешь его отгадывать
      ''')

###Функция проверки корректности введенных данных

def is_valid(x):
    flag = False
    while flag != True:
        print('Введите число от 1 до 100')
        x = input()
        if str(x).isdigit() == True:  ### Проверка на числа
            flag = True
        else:
            flag = False
            continue
        if int(x) in range(1,101):   ### Проверка на диапозон чисел
            flag = True
        else:    
            flag = False
            continue
    return x

def y_n(x):
    while True:
        print('Введите Y - если да и N - если нет')
        x = input()
        if x in 'ynYN':
            return x
        else:
            print('Введите Y - если да и N - если нет')

###Основной цикл программы
while True:
    popitki = 0

    num = random.randint(1, 100)

    while True:

        popitki += 1

        x = -1
        x = is_valid(x)
        x = int(x)
        
        ###Сравнение введенного числа с загаданным

        if  x < num:
            print('Ваше число меньше загаданного, попробуйте еще разок\n')
        elif x > num:
            print('Ваше число больше загаданного, попробуйте еще разок\n') 
        elif x == num:
            print('Вы угадали, поздравляем!')
            print('Число попыток:', popitki)
            break
    ### New game

    print('Ещё раз?')

    sogl = '0'
    sogl = y_n(sogl)
    
    if sogl in 'nN':
       print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
       break