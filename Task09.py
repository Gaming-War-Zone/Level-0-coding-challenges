def vowels_in_string(string):
    list_vowels = ['a','e','i','o','u']
    string = list(string)
    vowels = ''
    for letter in string:
        if letter in list_vowels:
            if letter not in vowels:
                vowels += letter.lower()

    vowels = ", ".join((vowels))
    print(f"Vowels: {vowels}")

vowels_in_string('Umuzi')
