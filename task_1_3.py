'''
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
'''

max_percent = 20
percent_list = []
percent = str("процент")

number_percent = int(input("Please, enter the percentage: "))

if number_percent == 1:
    element = print(f'{number_percent} {percent}')
elif number_percent < 5:
    element = print(f'{number_percent} {percent}{"а"}')
elif number_percent >= 5:
    element = print(f'{number_percent} {percent}{"ов"}')






