import random

lowDigit = 10 #границы
highDigit = 50
digit = 0 # загаданное число

countInput = 0 # количество попыток
win = False # угадал - флаг
playGame = True # продолжение игры
x = 0 # число вводимое пользователем
startScore = 100 # начальное количество очков
score = 0 # текущее количесво
maxScore = 0 # максимальное за подход

while(playGame):
    digit = random.randint(lowDigit,highDigit)
    print("-" * 30)
    countInput = 0
    score = startScore
    print("Число загаданно")
    while(not win and score > 0):
        print("-" * 30)
        print(f"заработанно очков {score}")
        print(f"рекорд {score}")

        x = ""
        while(not x.isdigit()): #чтобы пользователь ввел число
            x = input(f" Число от {lowDigit} до {highDigit}")
            if(not x.isdigit()):
                print("введите число")
        x = int(x)
        if(x == digit):
            win = True
        else:
            lenght = abs(x - digit)
            if(lenght < 3):
                print("очень горячо")
            elif(lenght < 5):
                print("горячо")
            elif (lenght < 10):
                print("тепло")
            elif (lenght < 15):
                print("прохлада")
            elif (lenght < 20):
                print("холодно")
            else:
                print("арктика")
            if(countInput == 7):
                score -= 10 # уменьшаем очки
                if(digit % 2 == 0):
                    print("Число четное")
                else:
                    print("Число не четное")
            elif(countInput == 6):
                score -= 8
                if(digit % 3 == 0):
                    print("Число делится на 3")
                else:
                    print("Число не делиться на 3")
            elif(countInput > 2 and countInput < 5):
                score -=2
                if(x > digit):
                    print( "Загаданное число меньше вашего")
                else:
                    print("Загаданное число больше вашего")
            score -=5
        countInput +=1
    print("*" * 40)
    if(x == digit):
        print("Победа")
    else:
        print("Вы проиграли")

    if(input("Enter - еще, 0 - выход ") == "0"):
        playGame = False
    else:
        win = False

    if(score > maxScore):
        maxScore = score

print("*" * 40)
