class NotEmailError(Exception):
    pass


class NotNameError(Exception):
    pass


tab = open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='tw', encoding='utf-8')
tab.write('name,email,old')
tab.write('\n')
tab.close()

with open('C:/Users/Артур/Desktop/skillbox/9/dz/registrations_.txt', mode='r', encoding='utf-8') as txt_file:
    for line in txt_file:
        line = line.replace(' ', ',')
        with open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='ta', encoding='utf-8') as chern:
            chern.write(line)

import csv

with open('C:/Users/Артур/Desktop/skillbox/9/dz/chernovik_.csv', mode='r', encoding='utf-8') as test:
    csv_test = csv.DictReader(test)
    for row in csv_test:
        name = row['name']
        email = row['email']
        old = row['old']
        if isinstance(name, str) and isinstance(email, str) and isinstance(old, str):
            if name.isalpha():
                if email.find('@') != -1 and email.find('.') != -1:
                    if 10 < int(old) < 99:
                        with open('C:/Users/Артур/Desktop/skillbox/9/dz/registrations_good.log', mode='ta',
                                  encoding='utf-8') as good:
                            good.write(' '.join((name, email, old, '\n')))
                    else:
                        try:
                            with open('C:/Users/Артур/Desktop/skillbox/9/dz/bad.txt', mode='ta',
                                      encoding='utf-8') as bad:
                                bad.write(' '.join((name, email, old, ' ValueError', '\n')))
                            raise ValueError('поле возраст НЕ является числом от 10 до 99')
                        except ValueError as exc:
                            print(f'возникла ошибочка {exc}, с параметром {exc.args}')
                else:
                    try:
                        with open('C:/Users/Артур/Desktop/skillbox/9/dz/bad.txt', mode='ta', encoding='utf-8') as bad:
                            bad.write(' '.join((name, email, old, ' NotEmailError', '\n')))
                        raise NotEmailError('поле email НЕ содержит @ и .(точку)')
                    except NotEmailError as exc:
                        print(f'возникла ошибочка {exc}, с параметром {exc.args}')
            else:
                try:
                    with open('C:/Users/Артур/Desktop/skillbox/9/dz/bad.txt', mode='ta', encoding='utf-8') as bad:
                        bad.write(' '.join((name, email, old, ' NotNameError', '\n')))
                    raise NotNameError('поле имени содержит НЕ только буквы')
                except NotNameError as exc:
                    print(f'возникла ошибочка {exc}, с параметром {exc.args}')
        elif isinstance(name, str) and isinstance(email, str) and old == None:
            try:
                with open('C:/Users/Артур/Desktop/skillbox/9/dz/bad.txt', mode='ta', encoding='utf-8') as bad:
                    bad.write(' '.join((name, email, ' ValueError', '\n')))
                raise ValueError('НЕ присутсвуют все три поля')
            except ValueError as exc:
                print(f'возникла ошибочка {exc}, с параметром {exc.args}')
