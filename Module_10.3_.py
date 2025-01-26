import threading
import time
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50,100)

            self.lock.acquire()
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            if self.balance >= 500:
                print("Баланс достиг 500 или более, разблокировка.")
                self.lock.release()
            else:
                self.lock.release()

            time.sleep(0.001)

    def take(self):

        for i in range(100):
            amount = random.randint(50,100)
            print(f'Запрос на {amount}.')
            self.lock.acquire()
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
                self.lock.release()
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.release()

            time.sleep(0.001)

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

