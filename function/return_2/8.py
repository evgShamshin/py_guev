def is_correct_bracket(txt):
    while '()' in txt:
        txt = txt.replace('()', '')
    return not txt

print(is_correct_bracket(input()))