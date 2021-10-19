# s1 = "Spam"
# s2 = "eggs"
# name = "Dosoy"
# last_name = "Orozbekov"
# middle_name = "Kanatbekovich"
# full_name = name + ' ' + last_name + ' ' + middle_name
# full_name_1 = name + ' ' + ((last_name + ' ') * 2)
# i1 = 1222222
# S = "Ваш сайт взлломали\nСвяжитесь с хакерами\nНе стоит звонить в полицию"
# S1 = r'C:\temp\new'


if __name__ == '__main__':
    import string

    # print(full_name)
    # print(full_name[0:6])
    # print(S)
    # print(len(name))
    # print(len(full_name))
    # print(len(str(i1)))
    # print((type(full_name_1))

    # my_str = 'abobabo'
    # string.find(my_str, 'abo')
    # string.find(my_str, 'abo', [1])
    # string.find(my_str, 'abo', [1, ], [2])

    # my_str = 'abobabo'
    # string.rfind(my_str, 'abo')
    # string.rfind(my_str, 'abo', [1])
    # string.rfind(my_str, 'abo', [1, ], [2])

    # my_str = 'barbarian'
    # my_str.index('bar')  # 0
    # my_str.index('bar', 1)  # 3
    # my_str.index('bar', 1, 2)  # ValueError

    # my_str = 'barbarian'
    # my_str = my_str.replace('bar', 'mur')
    # my_str = my_str.replace('mur', 'bur', 1)

    # print('1,2,3'.split(','))
    # print('1,2,3'.split(',', maxsplit=1))

    # print(''.isdigit())  # False
    # print('123'.isdigit())  # True

    # print('abc'.isalpha())  # True
    # print('123'.isalpha())  # False

    # print('!@#'.isalnum())  # False
    # print('abc'.isalnum())  # True
    # print('123'.isalnum())  # True

    # 'ВЕРХНИЙ UPPER'.isupper()  # True
    # 'нижний lower' .islower()  # True

    # '  '.isspace()  # True
    # '\n'.isspace()  # True
    # '!@#'.isspace()  # False
    # 'abc'.isspace()  # False

    # 'S'.istitle()  # True
    # 's'.istitle()  # False
    # 'SoMe СлОнов'.upper()  # SOME СЛОНОВ
    # 'SoMe СлОнов'.lower()  # some слонов

    # my_str = 'Discworld'
    # print(my_str.startswith('Mad'))  # False
    # print(my_str.startswith('Disc'))  # True

    # my_str = 'Discworld'
    # my_str.endswith('jockey')  # False
    # my_str.endswith('world')  # True

    # S.join method
    # A = ['red', 'green', 'blue']
    # print(' '.join(A))
    # print(''.join(A))
    # print('***'.join(A))

    # print(ord('b'))  # 97
    # print(ord('\u2020'))  # 8224

    # print(chr(98))  # b

    # 'нАЧАТЬ С ЗАГЛАВНОЙ '.capitalize()  # Начать с заглавной

    # ''.center(3, 'w')  # www
    # '1'.center(2, 'w')  # 1w
    # '1'.center(4, 'w')  # w1ww
    # '1'.center(0, 'w')  # 1
    # '1'.center(4)  # ' 1  '

    # В ходе смены регистра, буквы в нижнем регистре преобразуются в верхний, а буквы в верхнем преобразуются в нижний.
    # print('Кот ОбОрмот!'.swapcase())  # кОТ оБоРМОТ!

    # print("they're bill's friends from the UK".title())  # They'Re Bill'S Friends From The Uk
    # В результирующей строке первая буква каждого нового слова становится заглавной, в то время как остальные
    # становятся строчными. Такое написание характерно для заголовков в английском языке.

    # str = "this is string example....wow!!!"
    # print(str.zfill(40))  # 00000000this is string example....wow!!!

    # str = "this is string example....wow!!!"
    # print(str.ljust(50, '0'))  # this is string example....wow!!!000000000000000000

    # str = "this is string example....wow!!!"
    # print(str.rjust(50, '*'))  # ******************this is string example....wow!!!

    print('{}-{}-{}'.format(1, 2, 3))  # 1-2-3
    print('{}-{}-{}'.format(*[1, 2, 3]))  # 1-2-3
    print('-{:{fill}{align}8}-'.format('some', fill='+', align='^'))  # -++some++-
