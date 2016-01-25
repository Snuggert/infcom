import numpy as np


def print_string(string):
    for c in string:
        try:
            if(c.isupper() or c == ' ' or c == '_' or c == ":"):
                print(c, end="")
            else:
                print('?', end="")
        except UnicodeEncodeError:
            print('*', end="")
    print()


def write_string(string1, string2, filename):
    f = open(filename + ".csv", "w")
    print(", ".join(str(i) for i in range(0, len(string1))), file=f)
    for c in string1:
        try:
            if(c.isupper() or c == ' ' or c == '_' or c == ":"):
                print(c + ',', end="", file=f)
            else:
                print('?, ', end="", file=f)
        except UnicodeEncodeError:
            print('*, ', end="", file=f)
    print('', file=f)
    print('', file=f)
    for c in string2:
        try:
            if(c.isupper() or c == ' ' or c == '_' or c == ":"):
                print(c + ',', end="", file=f)
            else:
                print('?, ', end="", file=f)
        except UnicodeEncodeError:
            print('*, ', end="", file=f)
    print('', file=f)
    f.close()


def safe_chr(c):
    try:
        return chr(c)
    except ValueError:
        return '*'


def main():
    cipher = ""

    with open("ciphers/running_key_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()
    cipher = np.asarray(cipher.lower().split())
    cipher_int = cipher.astype(np.int32)

    key = ['_'] * len(cipher)
    text = ['_'] * len(cipher)

    print("|".join(list(cipher)))

    for i in range(2, cipher_int.size - 3, 4):
        text[i] = 'T'
        key[i] = safe_chr(cipher_int[i] - ord('T'))

        text[i + 1] = 'H'
        key[i + 1] = safe_chr(cipher_int[i + 1] - ord('H'))

        text[i + 2] = 'E'
        key[i + 2] = safe_chr(cipher_int[i + 2] - ord('E'))

        text[i + 3] = ' '
        key[i + 3] = safe_chr(cipher_int[i + 3] - ord(' '))

    for i, x in enumerate(cipher_int):
        if(x == 64):
            text[i] = ' '
            key[i] = ' '
        # elif(x == 97):
        #     text[i] = ' '
        #     key[i] = 'A'
        # elif(x == 101):
        #     key[i] = 'E'
        #     text[i] = ' '
        elif(x == 130):
            text[i] = 'A'
            key[i] = 'A'
        # elif(x == 146):
        #     text[i] = 'I'
        #     key[i] = 'I'

    print_string("TEXT:" + "".join(list(text)))
    print_string("KEY:" + "".join(list(key)))

    write_string(list(key), list(text), 'anus')

if __name__ == '__main__':
    main()
