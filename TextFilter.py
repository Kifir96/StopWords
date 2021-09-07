# 1) Составляем список запрещенных слов:
stop_words = ['блин', 'аладушек']
# 2) Вводим текст на проверку:
i_text = input("Введите текст: ")
# 3) Разбиваем введенный текст на куски длинной равные каждому запрещенному слову:
pieces = []
for word in stop_words:
    for i in range(len(i_text)):
        piece = i_text[i: i+len(word)]
        pieces.append(piece)
# 4)Сравниваем полученные куски со списком запрещенных слов:

for word in stop_words:
    for piece in pieces:
        if word == piece:
            print("Плохое слово - ", word)