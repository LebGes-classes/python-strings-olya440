import re

t = input('Введите текст: ')
text_right = re.findall(r'\w+',t)
text_right_0 = ' '.join(text_right)

new_word = []
w_c={}

for word in text_right_0:
    if 'A' <= word <= 'Z':
        new_word.append(chr(ord(word) + 32))
    elif 'А' <= word <= 'Я':
        new_word.append(chr(ord(word) + 32))
    elif word == 'Ё':
        new_word.append('ё')
    else:
        new_word.append(word)

result = ''.join(new_word)
ws = re.findall(r'\w+',result)

for w in ws:
    if w in w_c:
        w_c[w]+=1
    else:
        w_c[w]=1

sor = []

for w,c in w_c.items():
    sor.append((w,c))

for i in range(len(sor)):
    for j in range(i+1,len(sor)):
        if sor[i][1]<sor[j][1]:
            sor[i],sor[j]=sor[j],sor[i]

top5=sor[:5]

print("Топ 5 самых частых слов")

for w,c in top5:
    print(w,"-",c)
