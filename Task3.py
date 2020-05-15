# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите один из двенадцати месяцев года в виде целого числа от 1 до 12: '))

list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]

if month in list_winter:
    print('Вы выбрали один из месяцев зимы')
elif month in list_spring:
    print('Вы выбрали один из месяцев весны')
elif month in list_summer:
    print('Вы выбрали один из месяцев лета')
else:
    print('Вы выбрали один из месяцев осени')

dict_of_months = {'list_winter': [12, 1, 2], 'list_spring': [3, 4, 5],
                  'list_summer': [6, 7, 8], 'list_autumn': [9, 10, 11]}

if month in dict_of_months['list_winter']:
    print('Вы выбрали один из месяцев зимы')
elif month in dict_of_months['list_spring']:
    print('Вы выбрали один из месяцев весны')
elif month in dict_of_months['list_summer']:
    print('Вы выбрали один из месяцев лета')
else:
    print('Вы выбрали один из месяцев осени')
