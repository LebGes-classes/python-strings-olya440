s = input()
reserv_word = ''

for i in range(len(s) - 1, -1, -1):
    reserv_word += s[i]

w = []
word = ''

for i in s:
    if i == ' ':
        w.append(word)
        word = ''
    else:
        word += i

if word:
    w.append(word)

mir = ''

for a in range(len(w) - 1, -1, -1):
    mir += w[a] + (' ' if a != 0 else '')

print("Зеркальный порядок слов: ", mir)
print("Отзеркаленная строка: ", reserv_word)
