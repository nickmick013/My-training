import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open (file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f'время выполнения функций: {end_time - start_time:.5f} секунд')

start_time_threads = time()

threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


end_time_threads = time()
print(f'время выполнения потоков: {end_time_threads - start_time_threads:.5f} секунд')