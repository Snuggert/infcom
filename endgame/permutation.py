import webbrowser


def main():
    cipher = ""  # [1, 2, 4, 7]

    webbrowser.open("http://tholman.com/other/transposition/")

    with open("ciphers/permutation_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()
    cipher = cipher.lower()

    print(cipher)

if __name__ == '__main__':
    main()
