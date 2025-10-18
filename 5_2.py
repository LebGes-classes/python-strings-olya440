s = input('Введите текст на английском, заканчивавшийся точкой (больше точек не должно быть), также длина каждого слова должна быть небольше 20: ')

high_alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alf = 'abcdefghijklmnopqrstuvwxyz'

k = 0
t = []
text = ''
maxi = 0
encryp_text = ''

for w in s:
    if w in lower_alf or w in high_alf:
        text += w
    else:
        if text:
            t.append(text)
            text = ''

if text:
    t.append(text)

long_w = [word if len(word) <= 20 else word[0:20] for word in t]

for text in long_w:
    if len(text) > maxi:
        k = len(text)
        maxi = k
        
s_new = str(long_w)        

for text in s_new:
    if text in lower_alf:
        position = lower_alf.index(text)
        new_position = (position + k) % 26
        new_text = lower_alf[new_position]
        encryp_text += new_text
    elif text in high_alf:
        position = high_alf.index(text)
        new_position = (position + k) % 26
        new_text = high_alf[new_position]
        encryp_text += new_text
    else:
        encryp_text += text   
        

print("Зашифрованный текст:",encryp_text)
print("Число К:", k)
