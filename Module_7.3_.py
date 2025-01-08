class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(punct, '')
                    all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_position = {}
        for file_name, words in all_words.items():
            if word in words:
                word_position[file_name] = words.index(word) + 1
                return word_position

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
            return word_counts


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder3 = WordsFinder('Rudyard_Kipling_If.txt')
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

finder4 = WordsFinder('Mother_Goose_Monday’s_Child.txt')
print(finder4.get_all_words())
print(finder4.find('child'))
print(finder4.count('child'))



finder5 = WordsFinder('Walt_Whitman_O_Captain!_My_Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))

