from TextClass import Text
from ParsingFiles import parse_files

text1 = Text('1.txt')
text2 = Text('2.txt')

# print('text1:', text1)
# print('text2:', text2)

parse_files('1.txt', '2.txt')
