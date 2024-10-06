rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

rus_1337 = {
    'А':4,
    'Б':6,
    'В':8,
    'Г':'r',
    'Д':'D',
    'Е':'E',
    'Ё':'E',
    'Ж':')|(',
    'З':3,
    'И':'I/I',
    'Й':'I/I',
    'К':'K',
    'Л':'JI',
    'М':'M',
    'Н':'H',
    'О':'0',
    'П':'II',
    'Р':'P',
    'С':'C',
    'Т':'Τ',
    'У':'Y',
    'Ф':'∅',
    'Х':'}{',
    'Ц':'ll',
    'Ч':"'I",
    'Ш':'llI',
    'Щ':'lll',
    'Ъ':"'b",
    'Ы':'bI',
    'Ь':'b',
    'Э':'E',
    'Ю':'I0',
    'Я':'9I',
}
eng_1337 = {
    'A':4,
    'B':8,
    'C':'C',
    'D':'I)',
    'E':'E',
    'F':'F',
    'G':'G',
    'H':'H',
    'I':1,
    'J':'J',
    'K':'K',
    'L':'L',
    'M':'M',
    'N':"I\\I",
    'O':'0',
    'P':'P',
    'Q':'Q',
    'R':'R',
    'S':5,
    'T':'T',
    'U':'U',
    'V':"\\/",
    'W':"\\/\\/",
    'X':'}{',
    'Y':7,
    'Z':'Z',
}


def translate(in_str: str):
    in_cap_str = in_str.upper()
    out_str = ''

    for char in in_cap_str:
        if char in rus:
            out_str = f'{out_str}{rus_1337[char]}'
        elif char in eng:
            out_str = f'{out_str}{eng_1337[char]}'
        else:
            out_str = f'{out_str}{char}'

    return out_str


test1 = 'Я привёл вас посмотреть фильм "Ёжик в тумане"!'
test2 = 'Съешь же этих французских булок да выпей же чаю'
test3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

print(test3)
print(translate(test3))
