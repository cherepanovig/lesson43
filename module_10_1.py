# Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
# после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
import time
from time import sleep
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл на запись
        for i in range(1, word_count + 1):  #
            file.write(f'Какое-то слово № {i}\n')  # Записываем предложения построчно
            time.sleep(0.1)
            #print('Печатаем строку...')
    print(f'Завершилась запись в файл {file_name}')
    

time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
res_time = time_end - time_start
print(f'Время выполнения задачи: {res_time}')

# Вызов потоков
time_start = datetime.now()
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_end = datetime.now()
res_time = time_end - time_start
print(f'Время работы потоков: {res_time}')
