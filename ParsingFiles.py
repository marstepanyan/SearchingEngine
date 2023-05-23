from TextClass import Text
from WordClass import Word


def parse_files(file1, file2):
    text1 = Text(file1)
    text2 = Text(file2)

    words = text1 + text2
    parsed_results = {}

    for word in words:
        if word not in parsed_results:
            parsed_results[word] = set()
        if word in text1.words:
            parsed_results[word].add("1")
        if word in text2.words:
            parsed_results[word].add("2")

    with open('db.txt', 'w+') as out_file:
        for word, files in parsed_results.items():
            file_names = ','.join(sorted(files))
            word = Word(word).get_normalized_word()
            line = f"{word}:{file_names}\n"
            out_file.write(line)
