string = "C:/Фото/2013/Поход/vasya.jpg"
for i in string:
    if i.isdigit():
        print("Цифра")
    if i.isalpha():
        print("Буква")
    if i.islower():
        print("Строчная буква")
    if i.isupper():
        print("Заглавная буква")