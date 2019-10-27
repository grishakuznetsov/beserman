import re


def input_text():
    filename = input('Текст без исправлений без расширения: ')
    fileexp = filename + '.txt'
    with open(fileexp, 'r', encoding='utf-8') as f:
        textold = f.read()
        textold = textold.lower()
    filename = input('Рабочий текст без расширения: ')
    fileexp = filename + '.txt'
    with open(fileexp, 'r', encoding='utf-8') as f:
        textnew = f.read()
        textnew = textnew.lower()
    return textold, filename, textnew


def output_text(text1, text2, textold, filename):
    filename_out = filename + '_output.txt'
    with open(filename_out, 'w', encoding='utf-8') as f:
        f.write('Old text')
        f.write('\n' + textold)
        f.write('\n' + 'Cyrillic')
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
    cyralpha = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'ž',
                'з': 'z', 'ӟ': 'ǯ’', 'и': 'i', 'ӥ': 'i', 'й': 'j', 'к': 'k', 'л': 'l',
                'м': 'm', 'н': 'n', 'о': 'o', 'ӧ': 'ə', 'ө': 'å', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ў': 'w', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š', 'ъ': '',
                'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'u', 'я': 'a'}
    for key in cyralpha:
        text = text.replace(key, cyralpha[key])

    return text


def main():
    textold, filename, text = input_text()
    newtext = trans(text)
    output_text(text, newtext, textold, filename)


if __name__ == '__main__':
    main()
