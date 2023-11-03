string = "C:\DOC\Сайт\index.html"
s = string.rfind(".")
s1 = string[s+1:]
if s1=="htm"or  s1=="html" or s1=="php":
    print("Это веь-страница")
else:
    print("Что-то другое")