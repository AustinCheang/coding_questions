'''
Given a non-empty string of lowercase letters and a non-negative integer 
representing a key, write a function that returns a new string obtained 
by shifting every letter in  nput string by k positions in the alphabet, 
where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the 
letter z shifted by one returns the letter a.

Sample input:
    string = "xyz"
    key = 2

Sample output:
    "zab"
'''


def caesarCipherEncryptor_1(string, key):
    new_key = key % 26
    ans = []
    print(f'new_key: {new_key}')

    for letter in string:
        ans.append(get_new_letter_1(letter, new_key))

    return "".join(ans)


def get_new_letter_1(letter, key):
    new_letter_code = ord(letter) + key
    print(new_letter_code)

    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)


def caesarCipherEncryptor_2(string, key):
    new_key = key % 26
    ans = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    print(f'new_key: {new_key}')

    for letter in string:
        ans.append(get_new_letter_2(letter, new_key, alphabet))

    return "".join(ans)


def get_new_letter_2(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    print(f'new letter code: {new_letter_code}')

    return alphabet[new_letter_code] if new_letter_code <= 25 else alphabet[-1 + new_letter_code % 25]


string = "xyz"
key = 2

print(caesarCipherEncryptor_2(string, key))
