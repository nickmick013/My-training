team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


#Использование %:

print('В команде Мастера кода участников %s' % ':', team1_num, '!')
print('Итого сегодня в командах участников: %s' % team1_num, 'и', team2_num,'!')


#Использование format():


print('Команда Волшебники данных {} {} {}'.format('решила задач:', score_2, '!'))
print('Волшебники данных решили задачи за {} {} {}'.format(team1_time, 'с', '!'))


#Использование f-строк:

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print(f'Результат битвы: {result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')