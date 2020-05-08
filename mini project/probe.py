class NotEmailError(Exception):
    pass


class NotNameError(Exception):
    pass


tab = open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='tw', encoding='utf-8')
tab.write('name,email,old')
tab.write('\n')
tab.close()

import csv

with open('C:/Users/Артур/Desktop/skillbox/9/dz/registrations_.txt', mode='r', encoding='utf-8') as txt_file:
    for line in txt_file:
        line = line.replace(' ', ',')
        with open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='ta', encoding='utf-8') as chern:
            chern.write(line)

good = open('C:/Users/Артур/Desktop/skillbox/9/dz/registrations_good.log', mode='tw',
            encoding='utf-8')
bad = open('C:/Users/Артур/Desktop/skillbox/9/dz/bad.log', mode='tw',
           encoding='utf-8')


def oshib(name, email, old):
    if isinstance(name, str) and isinstance(email, str) and old == None:
        bad.write(' '.join((name, email, ' ValueError', '\n')))
        raise ValueError('НЕ присутсвуют все три поля')
    if isinstance(name, str) and email == None and old == None:
        bad.write(' '.join((name, ' ValueError', '\n')))
        raise ValueError('НЕ присутсвуют все три поля')
    if name == None and email == None and old == None:
        bad.write(' '.join((' ValueError', '\n')))
        raise ValueError('НЕ присутсвуют все три поля')
    elif not name.isalpha():
        bad.write(' '.join((name, email, old, ' NotNameError', '\n')))
        raise NotNameError('поле имени содержит НЕ только буквы')
    elif email.find('@') == -1 or email.find('.') == -1:
        bad.write(' '.join((name, email, old, ' NotEmailError', '\n')))
        raise NotEmailError('поле email НЕ содержит @ и .(точку)')
    elif 10 > int(old) or int(old) > 99:
        bad.write(' '.join((name, email, ' ValueError', '\n')))
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    elif isinstance(name, str) and isinstance(email, str) and isinstance(old, str):
        good.write(' '.join((name, email, old, '\n')))


with open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='r', encoding='utf-8') as test:
    csv_test = csv.DictReader(test)
    for row in csv_test:
        name = row['name']
        email = row['email']
        old = row['old']
        try:
            oshib(name, email, old)
        except ValueError as exc:
            print(f'возникла ошибочка {exc}, с параметром {exc.args}')
        except NotEmailError as exc:
            print(f'возникла ошибочка {exc}, с параметром {exc.args}')
        except NotNameError as exc:
            print(f'возникла ошибочка {exc}, с параметром {exc.args}')

good.close()
bad.close()
