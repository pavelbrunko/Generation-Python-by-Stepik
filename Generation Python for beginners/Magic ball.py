import random 

print('Привет мир! Я магический шар и я знаю ответ на любой твой вопрос')
print('Как тебя зовут?')
name = input()
print('Привет, ', name, '!', sep='')

def random_answers():
    answers = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
               'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси снова', 'Даже не думай', 
               'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно', 'Бесспорно', 'Предрешено', 
               'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
    num = random.randrange(20)
    answer = answers[num]
    print(answer)
    
flag = True

while flag == True:
    print('Каков твой вопрос?')
    question = input()
    random_answers()
    print('Есть ещё вопросы?')
    any_questions = input()
    if any_questions == 'Yes' or any_questions == 'Да' or any_questions == 'да' or  any_questions == 'yes':
        continue
    else:
        break
print('Возвращайся, если возникнут ещё вопросы!')
