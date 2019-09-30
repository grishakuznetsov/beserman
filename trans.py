import re


def input_text():
    filename = input('Filename WITHOUT .TXT: ')
    fileexp = filename + '.txt'
    with open(fileexp, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
    return text, filename


def output_text(text1, text2, filename):
    filename_out = filename + '_output.txt'
    with open(filename_out, 'w', encoding='utf-8') as f:
        f.write('Cyrillic')
        f.write('\n' + text1)
        f.write('\n' + 'Latin')
        f.write('\n' + text2)


def trans(text):
    palatal = {'ть': 'ț', 'ти': 'ți', 'тё': 'țo', 'тя': 'ța', 'тю': 'țu',
               'дь': 'ḑ', 'ди': 'ḑi', 'дё': 'ḑo', 'дя': 'ḑa', 'дю': 'ḑu',
               'сь': 'ś', 'си': 'śi', 'сё': 'śo', 'ся': 'śa', 'сю': 'śu',
               'зь': 'ź', 'зи': 'źi', 'зё': 'źo', 'зя': 'źa', 'зю': 'źu',
               'нь': 'ń', 'ни': 'ńi', 'нё': 'ńo', 'ня': 'ńa', 'ню': 'ńu',
               'ль': 'ĺ', 'ли': 'ĺi', 'лё': 'ĺo', 'ля': 'ĺa', 'лю': 'ĺu'
               }
    for key in palatal:
        text = text.replace(key, palatal[key])
    text = text.replace('лĺa', 'ĺĺa')
    cyralpha = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'o', 'ж': 'ž',
                'з': 'z', 'ӟ': 'ǯ’', 'и': 'i', 'ӥ': 'i', 'й': 'j', 'к': 'k', 'л': 'l',
                'м': 'm', 'н': 'n', 'о': 'o', 'ӧ': 'ə', 'ө': 'å', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ў': 'w', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č’', 'ш': 'š', 'ъ': '',
                'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'u', 'я': 'a'}
    for key in cyralpha:
        text = text.replace(key, cyralpha[key])

    return text


def main():
    text, filename = input_text()
    newtext = trans(text)
    output_text(text, newtext, filename)


if __name__ == '__main__':
    main()
