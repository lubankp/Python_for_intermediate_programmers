import os

path = r'C:\Users\Dell\Desktop\Python\Python_dla_sredniozaawansowanych\Section2.12\plik.txt'


def count_words(path):
    with open(path, 'r') as file:
        line = file.read()
        words = line.split()
    return len(words)

result = os.path.isfile(path) and count_words(path)
print(result)