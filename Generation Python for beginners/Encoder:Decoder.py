print('Добрый день! Вы хотите защифровать или дешифровать текст?')

flag = True

while flag == True:
    doing = input()
    if doing == 'Зашифровать' or doing == 'зашифровать' or doing == 'Дешифровать' or doing == 'дешифровать' or doing == 'Encrypt' or doing == 'encrypt' or doing == 'Decrypt' or doing == 'decrypt':
        flag == False
        break
    elif doing != 'Зашифровать' or doing != 'зашифровать' or doing != 'Дешифровать' or doing != 'дешифровать' or doing == 'Encrypt' or doing == 'encrypt' or doing == 'Decrypt' or doing == 'decrypt':
        print('Не совсем понял, повторите, пожалуйста')

print('Введите текст для шифрования/дешифрования')
text = input()

print('Введите код шифрования/дешифрования')
n = int(input())

text = list(text)

alph_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alph_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Шифратор рус.
if doing == 'Зашифровать' or doing == 'зашифровать':
    new_text = []
    for i in range(len(text)):
        sign = text[i]
        if sign.isalpha() == True:
            where_in_alph = alph_ru.index(sign.lower())
            if where_in_alph + n > 31:
                new_sign = alph_ru[where_in_alph + n - 31]
            else:
                new_sign = alph_ru[where_in_alph + n]
            if sign.isupper() == True:
                new_sign_1 = new_sign.upper()
            else:
                new_sign_1 = new_sign            
            new_text.extend(new_sign_1)
        else:
            sign == sign
            new_text.extend(sign)
    print(''.join(new_text))

#Шифратор анг.
if doing == 'Encrypt' or doing == 'encrypt':
    new_text = []
    for i in range(len(text)):
        sign = text[i]
        if sign.isalpha() == True:
            where_in_alph = alph_eng.index(sign.lower())
            if where_in_alph + n > 25:
                new_sign = alph_eng[where_in_alph + n - 26]
            else:
                new_sign = alph_eng[where_in_alph + n]
            if sign.isupper() == True:
                new_sign_1 = new_sign.upper()
            else:
                new_sign_1 = new_sign            
            new_text.extend(new_sign_1)
        else:
            sign == sign
            new_text.extend(sign)
    print(''.join(new_text))

#Дешифратор рус.
if doing == 'Дешифровать' or doing == 'дешифровать':
    new_text = []
    for j in range(len(text)):
        sign = text[j]
        if sign.isalpha() == True:
            where_in_alph = alph_ru.index(sign.lower())
            if where_in_alph - n < 0:
                new_sign = alph_ru[where_in_alph - n + 31]
            elif where_in_alph - n == 0:
                new_sign = alph_ru[where_in_alph - n + 31]
            elif where_in_alph - n == 31:
                new_sign = alph_ru[where_in_alph - (n - 1) + 32]            
            else:
                new_sign = alph_ru[where_in_alph - n]
            if sign.isupper() == True:
                new_sign_1 = new_sign.upper()
            else:
                new_sign_1 = new_sign            
            new_text.extend(new_sign_1)            
        else:
            sign == sign
            new_text.extend(sign)
    print(''.join(new_text))
        
#Дешифратор анг.
if doing == 'Decrypt' or doing == 'decrypt':
    new_text = []
    for j in range(len(text)):
        sign = text[j]
        if sign.isalpha() == True:
            where_in_alph = alph_eng.index(sign.lower())
            if where_in_alph - n < 0:
                new_sign = alph_eng[where_in_alph - n + 26]
            elif where_in_alph - n == 0:
                new_sign = alph_eng[where_in_alph - n + 25]
            elif where_in_alph - n == 25:
                new_sign = alph_eng[where_in_alph - n + 25]            
            else:
                new_sign = alph_eng[where_in_alph - n]
            if sign.isupper() == True:
                new_sign_1 = new_sign.upper()
            else:
                new_sign_1 = new_sign            
            new_text.extend(new_sign_1)            
        else:
            sign == sign
            new_text.extend(sign)
    print(''.join(new_text))