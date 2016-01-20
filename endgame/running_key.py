import numpy as np


def main():
    cipher = ""

    with open("ciphers/running_key_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()
    cipher = np.asarray(cipher.lower().split())
    cipher_int = cipher.astype(np.int32)

    key = ['_'] * len(cipher)
    text = ['_'] * len(cipher)

    for i, x in enumerate(cipher_int):
        if(x == 64):
            text[i] = ' '
            key[i] = ' '
        elif(x == 97):
            text[i] = ' '
            key[i] = 'A'
        elif(x == 130):
            text[i] = 'A'
            key[i] = 'A'

    print(" ".join(list(cipher)))
    print("".join(list(key)))
    # print(chr(cipher[0] - ord('Z')))

if __name__ == '__main__':
    main()
