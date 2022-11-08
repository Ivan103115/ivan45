#1
#def first_word(words='Hello World'):
#    if type(words) == str:
#        first_word = words.split()
#        return first_word[0]
#    elif type(words) != str:
#        return False
#print(first_word())
#2
# def sum1(*args):
#     return (int(sum(args) / len(args)))

# print(sum1())

#3
def level(password):
    if len(password) > 6 and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False


print (level(input ('Ведите пароль')))















