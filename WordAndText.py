class Word:
    def __init__(self, str_word: str):
        self.val = str_word

    def make_lowercase(self):
        return Word(self.val.lower())

    def remove_symbols(self):
        special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        if not self.val.isalpha():
            for i in special_characters:
                self.val.replace(i, '')
        return Word(self.val)

    def is_word_in_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if self.val in line:
                    return True
        return False

    def normalize(self, file_path):
        if self.is_word_in_file(file_path):
            return self.val


class Text:
    def __init__(self, file_path):
        self.file = file_path
        self.words = []
        with open(file_path, 'r') as file:
            self.file_contents = file.read()

    def __repr__(self):
        file_for_normalizing = 'words_alpha.txt'

        for element in self.file_contents.split():
            lowercase_element = Word(element).make_lowercase()
            clean_element = lowercase_element.remove_symbols()
            normalized_element = clean_element.normalize(file_for_normalizing)

            if normalized_element:
                self.words.append(normalized_element)

        return str(self.words)


text1 = Text('1.txt')
text2 = Text('2.txt')
print('text1:', text1)
print('text2:', text2)
