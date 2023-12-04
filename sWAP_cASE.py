def swap_case(s):
    new_word = ""
    for letter in s:
        if letter == letter.lower():
            new_word += letter.upper()
        elif letter == letter.upper():
            new_word += letter.lower()
    return new_word

s = input()
result = swap_case(s)
print(result)
