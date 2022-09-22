# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


from random import randint

def input_dat(name):
    x = int(input(f"{name}, сколько возьмёте конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, не правильно, нужно взять хотя бы одну и не больше чем 28 конфет: "))
    return x


def p_print(name, candys, value):
    print(f"Ходил {name}, он взял {candys} конфет. На столе осталось {value} конфет.")

player1 = input("Первый игрок, введите своё имя: ")
player2 = input("Второй игрок, введите своё имя: ")
value = int(input("Введите количество конфет на столе: "))

flag = randint(0,2)

if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")


while value > 28:
    if flag:
        candys = input_dat(player1)        
        value -= candys
        flag = False
        p_print(player1, candys, value)
    else:
        candys = input_dat(player2)        
        value -= candys
        flag = True
        p_print(player2, candys, value)

#а) А это с глупым ботом:

# while value > 28:
#     if flag:
#         candys = input_dat(player1)        
#         value -= candys
#         flag = False
#         p_print(player1, candys, value)
#     else:
#         candys = randint(1,29)        
#         value -= candys
#         flag = True
#         p_print(player2, candys, value)


#b) А это бот поумнел и если ходит первым - не оставляет шансов на победу. корректно ходить вторым научить пока не могу.

# flag = 1

# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Первым ходит {player2}")

# while value > 28:
#     if flag:
#         candys = input_dat(player1)        
#         value -= candys
#         flag = False
#         p_print(player1, candys, value)
#     else:
#         candys = value % 29       
#         value -= candys
#         flag = True
#         p_print(player2, candys, value)


if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
    