# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_enc_1.txt','r') as file:
    my_list = file.readline()
    

def encode(a_str): 
    encoding = ""
    i = 0   
    while i < len(a_str):        
        count = 1 
        while i + 1 < len(a_str) and a_str[i] == a_str[i + 1]:
            count += 1
            i += 1        
        encoding += str(count) + a_str[i]
        i += 1 
    return encoding

encodeded_val = encode(my_list)
print(encodeded_val)


with open('file_enc_2.txt', 'w') as file:
    file.write(encodeded_val)



with open('file_dec_1.txt','r') as file:
    my_list1 = file.readline()


def decode(data):
    decoding = '' 
    count = ''    
    for elements in data:        
        if elements.isdigit():
            count += elements 
        else:
            decoding += elements * int(count) 
            count = '' 
    return decoding

decoded_val = decode(my_list1) 
print(decoded_val)

with open('file_dec_2.txt', 'w') as file:
    file.write(decoded_val)

