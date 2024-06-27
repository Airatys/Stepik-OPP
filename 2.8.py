# Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
# Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.
# Формат входных данных
# На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.
# Формат выходных данных
# Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате DD.MM.YYYY.
# Примечание 1. Гарантируется, что подаваемые год и месяц всегда корректны.

import calendar
from datetime import*

year = int(input())
month = int(input())
count = 0
for i in calendar.monthcalendar(year, month):
    if i[3] != 0:
        count += 1
        if count == 4:
            print(datetime(year, month, i[3]).strftime('%d.%m.%Y'))
            break
        
# через поиск первого четверга и прибавлением 3 недель       

from datetime import date

year, month = int(input()), int(input())

for i in range(1, 8):
    if date(year, month, i).isoweekday() == 4:
        day = i + 21

print(date(year, month, day).strftime('%d.%m.%Y'))