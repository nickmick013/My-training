

class Video:

    def __init__(self, title, duration, adult_mode = bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __eq__(self, other):
        return self.title == other.title
    def __contains__(self, item):
        return item in self.title

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname
    def __hash__(self):
        return hash(self.password)
    def __int__(self):
        return self.age

import time

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user == user.nickname and password == user.password:
                self.current_user = user
                return

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword):
        titles = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                titles.append(video.title)
        return titles

    def watch_video(self, film):
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if film in video.title:
                    for i in range(1, 11):
                        print(i, end = ' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')





if __name__ == '__main__':
# Код для проверки работы классов
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # "Войдите в аккаунт..."
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация пользователя
ur.watch_video('Для чего девушкам парень программист?')  # "Вам нет 18 лет..."
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация пользователя с доступом к видео
ur.watch_video('Для чего девушкам парень программист?')  # Просмотр видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Попытка зарегистрироваться с существующим никнеймом
print(ur.current_user.nickname)  # 'urban_pythonist'

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # "Видео не найдено."









# if __name__ == '__main__':
#     database = Database()

