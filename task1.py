# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# my_str = 'Мы неабв очень любим Питон иабв Джавуабв'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))


my_str ='Кудабв уехал цирк он абвыл еще абвчера И абветер не успел со стен сорабвабвть абвфиши'.split()

new_str = []
fragment = ('абв')
for word in my_str:
    if fragment not in word:
        new_str.append(word)

print(' '.join(new_str))


