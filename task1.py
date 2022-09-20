# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# my_str = 'Мы неабв очень любим Питон иабв Джавуабв'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))


my_str ='Куда уехал цирк он был еще вчера И ветер не успел со стен сорвать афиши'.split()

new_str = []
fragment = ('а' or 'б' or 'в')
for word in my_str:
    if fragment not in word:
        new_str.append(word)

print(' '.join(new_str))


