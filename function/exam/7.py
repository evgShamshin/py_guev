def check_all_alpha(txt):
    txt = txt.replace(' ', '')
    txt = txt.lower()
    if len(set(txt)) == 26:
        return True
    else:
        return False

print(check_all_alpha(input()))