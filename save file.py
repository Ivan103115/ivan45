# print('введите температуру в областях')
# print('Ош')  #вывод для обозначения области
# Ош = int(input())  #для ввода температуры в области
# print('Чуй')  #вывод для обозначения области
# Чуй = int(input())  #для ввода температуры в области
# print('Баткен')  #вывод для обозначения области
# Баткен = int(input())  #для ввода температуры в области
# print('Джалал-Абат')  #вывод для обозначения области
# ДжалалАбат = int(input())  #для ввода температуры в области
# print('Нарын')  #вывод для обозначения области
# Нарын = int(input())  #для ввода температуры в области
# print('Ыссык-Куль')  #вывод для обозначения области
# ЫссыкКуль = int(input())  #для ввода температуры в области
# print('Талас')  #вывод для обозначения области
# Талас= int(input())  #для ввода температуры в области
# summa = (Ош + Чуй + Баткен + ДжалалАбат + Нарын +ЫссыкКуль + Талас)  #подсчёт температуры всех областей
# avenger =(summa // 7)  # сумму делим на области чтобы узнать средний показатель температуры
# print('средний показатель температуры воздуха в Кыргызстане',avenger,'c°')#вывод



# print('Напиши время суток')
# time = input()
# if time == 'утро'or time == 'morning':
#       print("доброе утро")
# elif time =='день'or time == 'day ':
#       print('добрый день')
# elif time =='вечер' or time == 'evening':
#       print('добрый вечер')
# elif time == 'ночь' or time == 'night':
#       print('доброй ночи')
# else:
#     print('здравствуйте')

# password1 , password2 = input('введите пароль:'),
# if not password1.isdigit() and not password1.isalpha() and len(password1)>= 8:
#     print('надёжный пароль')
#     password2 = input('повторите пароль:')
# if password1 == password2:
#     print('ok')
# else:
#     print('bad')

# date=int(input("Введите день рождения:"))
#
# month=int(input("Введите месяц рождения:"))
#
# if (date>=21 and date<=31 and month==3) or( month==4 and date>=1 and date<=19):
#     print("Знак зодиака:Овен")
#
# elif (date>=20 and date<=30 and month==4) or( month==5 and date>=1 and date<=20):
#     print("Знак зодиака:Телец")
#
# elif (date>=21 and date<=31 and month==5) or( month==6 and date>=1 and date<=21):
#     print("Знак зодиака:Близнецы")
#
# elif (date>=22 and date<=30 and month==6) or( month==7 and date>=1 and date<=22):
#     print("Знак зодиака:Рак")
#
# elif (date>=23 and date<=31 and month==7) or( month==8 and date>=1 and date<=22):
#     print("Знак зодиака:Лев")
#
# elif (date>=23 and date<=31 and month==8) or( month==9 and date>=1 and date<=22):
#     print("Знак зодиака:Дева")
#
# elif (date>=23 and date<=30 and month==9) or( month==10 and date>=1 and date<=23):
#     print("Знак зодиака:Весы")
#
# elif (date>=24 and date<=31 and month==10) or( month==11 and date>=1 and date<=22):
#     print("Знак зодиака:Скорпион")
#
# elif (date>=23 and date<=30 and month==11) or( month==12 and date>=1 and date<=21):
#     print("Знак зодиака:Стрелец")
#
# elif (date>=22 and date<=31 and month==12) or( month==1 and date>=1 and date<=20):
#     print("Знак зодиака:Козерог")
#
# elif (date>=21 and date<=31 and month==1) or( month==2 and date>=1 and date<=18):
#     print("Знак зодиака:Водолей")
#
# elif (date>=19 and date<=29 and month==2) or( month==3 and date>=1 and date<=20):
#     print("Знак зодиака:Рыбы")
# else:
#
#
# for a in range(1,11):
#     for b in range(1,11):
#         for c in range(1,11):
#             for d in range(1,11):
#                 for e in range(1,11):
#                     print(f'{a} {b} {c} {d} {e}' )




# word = input('введите слово -->')
# vowels = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y" or\
#        letter == "A" or letter == "E" or \
#        letter == "I" or letter == "O" or \
#        letter == "U" or letter == "Y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))








# END ЭТО ОТМЕНА ПЕРЕНОСА СТРОКИ

# while True:
#     word = input('введите слово -->')
#     if word == 1:
#         break
#     vowels =('eyuioaеыаоэяию')
#     consonants =('qwrtpsdfghjklzxcvbnmцкнгшщзхфвпрлджчсмтб')
#     колво =0
#     гласные =0
#     согласные = 0
#     for vowels in word:
#         гласные =+ 1
#
#         for consonants in word:
#          coгласные =+ 1
#
#          for vowels in word:
#              колво = + 1
#
#              for consonants in word:
#                  колво = + 1
#         print('общее кол-во букв',колво)
#         print('согласных букв',consonants)
#         print('гласных букв',vowels)


# d = 'eyuioaуеыаоэяию'
# p = 'йцкнгшщзхфвпрлджчсмтбqwrtpsdfghjklzxcvbnm'
# while True:
#     a = 0
#     b = 0
#     t = 0
#     print('\nдля остановки напишите "stop!"')
#     c = input(" \nвведите слово")
#     y = c.lower()
#     for i in y:
#         if (i in d) or (i in p):
#             t = int(t)
#             t += 1
#         if i in d:
#             a = int(a)
#             a += 1
#         if i in p:
#             b = int(b)
#             b += 1
#     if y == 'stop!':
#         break
#     h = 100 * a / (a + b)
#     q = 100 * b / (a + b)
#     print(f"слово - {c}\nвсего букв - {t}\nгласные - {a}\nсогласные - {b}\nпроцент гласных - {round(h, 2)}%", end = '')
#     print(f"\nпроцент согласных - {round(q, 2)}%", end='')



# data_tuple = ('h',6.13,'C','e','T',True,'k','e',3,'e',1,'g')
# letters = []
# numbers = []
# print(data_tuple)
# floating = []#создал 2 списка для облегчения
# bools = []
# letters =[i for i in data_tuple if type(i) == str]
# bools =[i for i in data_tuple if type(i) == bool]
# numbers =[i for i in data_tuple if type(i) == int]
# floating =[i for i in data_tuple if type(i) == float]
# letters +=bools
# numbers += floating#соеденил списки
# numbers.pop(-1)
# numbers.sort()
# letters.reverse()
# letters[1] = 'G'
# letters[7] = 'c'
# numbers.append(2)
# numbers[1] = 2
# numbers[2] = 3
# print(numbers)
# numbers[1] = 4
# numbers[2] = 9 #до этого момента изменил буквы и цифры
# numbers=tuple(numbers)
# letters=tuple(letters)
# print(numbers)
# print(letters)

# data = ("O!","Megacom", "0705" ,"Beelie", "0550", "0770","Katel", "0510","Fonex", "0543")
# designations = []
# codes = []
# for i in data:
#     if i.startswith('0'):
#         codes.append(i)
#     else:
#         designations.append(i)
# operators = zip(designations, codes)
# operators = dict(operators)
# operators.pop('Katel',None)
# operators.pop('Fonex',None)
# operators['O!']  = '0705', '0700','0500'
# operators['Megacom'] = '0550','0999','0555'
# operators['Beelie'] = '0770','0222','0777'
# print(operators)

# def greeting(name):
#     print('hello', name)
#
#
#
# greeting('john')
#
# def greeting(name,surname):
#     print('hello', name,surname)
#
#
#
# greeting('john','walker')
# greeting('sam','tyson')

# def sum1(*gg):
#     return sum(gg)
# print(sum1())


# def first_word(words=input('')):
#    if type(words) == str:
#        first_word = words.split()
#        return first_word[0]
#    elif type(words) != str:
#        return False
# print(first_word())


# def middle(*args):
#     return (sum(args) // len(args))
# print(middle(10.5, 20))



# def level(password):
#     if len(password) > 6 and not password.isdigit() and not password.isalpha():
#         return True
#     else:
#         return False
#
#
# print (level(input ('Ведите пароль')))

# def up_letter(word: str):
#     return word.title()
#
# def last_up(word):
#     return word[:-1]+word[-1].title()
#
#
#
# def show_words(words_list: list,func):
#     for i in words_list:
#         print(func(i))
#
# object = ['python', 'geektech', 'bishkek']
# show_words(object, up_letter)
# show_words(object, last_up)

# x=lambda *args: int (sum(args) // len(args))
# print(x(12,89))

# ten=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# evens=list(filter(lambda x: x % 2 == 0, ten))
# print(tuple(map(lambda x: x ** 2, evens)))
# print('введите stop для выхода')
#
# def surf_for_index(ten=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)):
#     while True:
#         try:
#             users_index = int(input())
#             print(ten[users_index])
#         except:
#             print("Введите правильный индекс, доступные индексы от 0 до 9")
#         finally:
#             users_index = "stop"
#             break
# print(surf_for_index())


# file = open('file.txt','w',encoding='UTF-8')
# file.write()
# file.close()
#
# with open('file.txt','r' )as file:
#    print(file.readline())

# left = 1
# right = 100
# a = 'больше, меньше, да'
# while True:
#     current = (left+right)//2
#     is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
#     if is_right.lower() == 'да':
#         print('Я его угадал!')
#         break
#     elif is_right == 'больше':
#         left = current + 1
#     elif is_right == 'меньше':
#         right = current - 1
#     else:
#         print('введите коректный ответ  да  больше  меньше')

# class Hero:
#     head=1
#     abilyty=True
#     def __init__(self,name,nickname,hp,damage):
#         self.name=name
#         self.nickname=nickname
#         self.hp=hp
#         self.damage=damage
#     def heal(self):
#         print(self.hp +100)
#
#     def two_damage(self):
#         print(self.damage*2)
#
#     def gritting(self):
#         print(f"my name is {self.name}")
#
#     def brand_phrase(self):
#         print('good will win')
# h1=Hero('optimus','prime',10000,100)
# h2=Hero('bakay','bakaevich',1,100)
# h3=Hero('org','boss',1000000,57647453)
# h4=Hero('optical','suprime',100990,10078)
#
# h1.two_damage()
# h2.heal()
# h3.gritting()
# h4.brand_phrase()

#git add.
#git commit -m название файла
# git push



'git init'
'добавляет в гит ваш проект'
''
'git remote add origin .....'
'связывает ваш проект с вашим репозиторием'
''
'.gitignore:'
'    .gitignore'
'    .idea'
'    __pycache__/'
'    venv'
'скрывает ненужные файлы от репозитория'
''
''
'git add .'
'добавляет изменения'
''
'git commit -m '''
'даёт имя'
'сохраняет изменения'
''
'git push origin master/main'
'пушит ваш проект в ваш репозиторий'
''
''
'git rm --cached название файла'
'удоляет файл из репо'
''
'git rm --cached -r название папки'
'удаляет папку из репо'''
''
''
'git clone ссылка репозитория'
'клонирует проект'

