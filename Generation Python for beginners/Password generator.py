import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
strange_punctuation = 'il1LoO0'

chars = []

print('Сколько паролей нужно сгенерировать?')
num_of_passwords = int(input())
print('Какова необходимая длина паролей?')
len_of_password = int(input())
print('Включать ли цифры?')
dig = input()
print('Включать ли прописные буквы?')
l_let = input()
print('Включать ли строчные буквы?')
u_let = input()
print('Включать ли прочие символы?')
sym = input()
print('Исключать ли неоднозначные символы?')
other_sym = input()

if dig == 'Yes' or dig == 'Да' or dig == 'да' or dig == 'yes':
    chars.extend(digits)
if l_let == 'Yes' or l_let == 'Да' or dig == 'да' or dig == 'yes':
    chars.extend(lowercase_letters)
if u_let == 'Yes' or u_let == 'Да' or dig == 'да' or dig == 'yes':
    chars.extend(uppercase_letters)
if sym == 'Yes' or sym == 'Да' or dig == 'да' or dig == 'yes':
    chars.extend(punctuation)
if other_sym == 'Yes' or other_sym == 'Да' or dig == 'да' or dig == 'yes':
    chars.remove('i')
    chars.remove('l')
    chars.remove('1')
    chars.remove('L')
    chars.remove('o')
    chars.remove('O')
    chars.remove('0')
    
def password_generator():
    for i in range(num_of_passwords):
        new_pass = ""
        for j in range(len_of_password):
            new_num = random.randrange(0, len(chars))
            new_pass += chars[new_num]
        print(new_pass)
        
password_generator()

    
