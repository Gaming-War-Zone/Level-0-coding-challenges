def common_letters(string1, string2):
    com_char = ''
    string1 = list(string1)
    for i in string1:
        if i in string2:
            if i not in com_char:
                com_char += i
                
    com_char = ", ".join((com_char))
    print(f"Common letters: {com_char}")

common_letters('house', 'computers')
