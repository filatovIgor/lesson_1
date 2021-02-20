'''
Необходимо вывессти информацию о промежутке времени в зависимости от его продолжительности duration в секундах
до минуты: <s>сек
до часа: <m>мин <s>сек
до суток: <h>час <m>мин <s>cek
до месяца: <d>сут <h>час <m>мин <s>cek
'''

sec_in_min = 60
sec_in_hour = sec_in_min * 60
sec_in_day = sec_in_hour * 24
sec_in_month = sec_in_day * 30


duration = int(input("Please, enter the time interval in second: "))
min = int(duration / sec_in_min)
hour = int(duration / sec_in_hour)
day = int(duration / sec_in_day)

if duration < sec_in_min:
    print("Duration:", duration, "сек")
elif duration < sec_in_hour:
    print("Duration:", min, "мин", duration - (min * sec_in_min), "сек")
elif duration < sec_in_day:
    print("Duration :", hour, "час", int((duration - (hour * sec_in_hour)) / sec_in_min), "мин", duration - (min * sec_in_min), "сек")
elif duration < sec_in_month:
    print("Duration :", day, "сут", int((duration - (day * sec_in_day)) / sec_in_hour), "час", int((duration - (hour * sec_in_hour)) / sec_in_min), "мин", int(duration - (min * sec_in_min)), "сек")

# print("Duration:", duration, "сек")
# print("Duration:", min, "мин", duration - (min * sec_in_min), "сек")
# print("Duration :", day, "сут", int((duration - (day * sec_in_day)) / sec_in_hour), "час", int((duration - (hour * sec_in_hour)) / sec_in_min), "мин", int(duration - (min * sec_in_min)), "сек")
# print("Duration :", day, "сут", int((duration - (day * sec_in_day)) / sec_in_hour), "час", int((duration - (hour * sec_in_hour)) / sec_in_min), "мин", int(duration - (min * sec_in_min)), "сек")



