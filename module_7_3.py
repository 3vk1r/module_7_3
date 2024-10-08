class WordsFinder:
    def __init__(self, *filename):
        self.file_names = filename

    def get_all_words(self):
        all_words = {}
        punctuation = ['.', ',', '=', '?', '!', ';', ' - ', ':']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for p in punctuation:
                    text = text.replace(p, ' ')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}

        all_word = self.get_all_words()
        word = word.lower()
        for name, words in all_word.items():
            if word in words:
                result[name] = words.index(word) + 1
            else:
                result[name] = None
        return result

    def count(self, word):
        result = {}

        all_word = self.get_all_words()
        word = word.lower()
        for name, words in all_word.items():
            result[name] = words.count(word)
        return result





finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
