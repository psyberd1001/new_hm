import random

number_1 = random.randint(0, 100)
print(number_1)

def function_seek_beenare(number_2):
    element_1 = 0
    element_last = 100
    index = -1
    count_1 = 0
    while (element_1 <= element_last) and (index == -1):
        mid = (element_1+element_last)//2
        count_1 = count_1 + 1
        if number_2 == mid:
            index = mid
            print('Вы выиграли, искомый элемент: --', index)
            break
        else:
            if mid > number_2:
                element_last = mid - 1
                print('ЖИЗНЬ ЗА НЕРЗУЛА', element_last, 'Число итераций', count_1)  # где "ЖИЗНЬ ЗА НЕРЗУЛА" расшифровывается как число больше чем задано
            else:
                element_1 = mid + 1
                print('НУЖНО БОЛЬШЕ ЗОЛОТА', element_1, 'Число итераций', count_1)  # Где "НУЖНО БОЛЬШЕ ЗОЛОТА" расшифровывается как число меньше чем задано
    return index

function_seek_beenare(number_1)
