d = 'eyuioaуеыаоэяию'
p = 'йцкнгшщзхфвпрлджчсмтбqwrtpsdfghjklzxcvbnm'
while True:
    a = 0
    b = 0
    t = 0
    print('\nдля остановки напишите "stop!"')
    c = input(" \nвведите слово")
    y = c.lower()
    for i in y:
        if (i in d) or (i in p):
            t = int(t)
            t += 1
        if i in d:
            a = int(a)
            a += 1
        if i in p:
            b = int(b)
            b += 1
    if y == 'stop!':
        break
    h = 100 * a / (a + b)
    q = 100 * b / (a + b)
    print(f"слово - {c}\nвсего букв - {t}\nгласные - {a}\nсогласные - {b}\nпроцент гласных - {round(h, 2)}%", end = '')
    print(f"\nпроцент согласных - {round(q, 2)}%", end='')

