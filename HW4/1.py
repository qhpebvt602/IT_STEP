from random import randint
# import - расширение возможностей с помощью библеотек

list=[]
#  списки list это массив данных
print('символы не должны повторяться')
list.append(input('введите первый вариант:  '))
list.append(input('введите втророй вариант: '))
list.append(input('введите третий вариант: '))
list.append(input('введите четвертый вариант: '))
list.append(input('введите пятый вариант: '))
# inpute - ввод с клавиатуры
# list.append - добавления элемента (варианта) в масив
print(list[randint(0, len(list)-1)])
# последний символ имеет индекс -1
