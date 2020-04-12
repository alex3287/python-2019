def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower())==1:
            return i
    s = ''
    return s

print(first_non_repeating_letter('sSDf'))