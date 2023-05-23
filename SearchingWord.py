from WordClass import Word


search_word = str(input('Enter the word for search:'))


def search_word_in_db(word, db_file):
    norm_word = Word(word).get_normalized_word()
    with open(db_file, 'r') as db:
        for line in db:
            line = line.strip()
            if line.startswith(str(norm_word) + ":"):
                file_names = line.split(":")[1]
                return file_names.split(',')
    return None


print(search_word_in_db(search_word, 'db.txt'))
