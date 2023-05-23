from WordClass import Word


class Text:
    def __init__(self, file_path):
        self.file = file_path
        self.words = []
        with open(file_path, 'r') as file:
            self.file_contents = file.read()

        for element in self.file_contents.split():
            word = Word(element)
            if word.get_normalized_word():
                self.words.append(word.val)

    def __repr__(self):
        return str(self.words)

    def __add__(self, other):
        return self.words + other.words
