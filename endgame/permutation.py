import webbrowser


def main():
    cipher = ""  # [1, 2, 4, 7]
    cipher_dict = {}
    cipher_frequency = {}

    webbrowser.open("http://tholman.com/other/transposition/")

    with open("ciphers/permutation_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()
    cipher = cipher.lower()

    for c in cipher:
        if(c in cipher_dict.keys()):
            cipher_dict[c] += 1
        else:
            cipher_dict[c] = 1

    for c in cipher_dict:
        cipher_frequency[c] = (cipher_dict[c] / float(len(cipher))) * 100

    print("Number of different chars: ", len(cipher_dict))
    print("Frequencies of chars in Cipher: ")

    for line in sorted(cipher_frequency.items(), key=lambda x: x[1],
                       reverse=True):
        print(line[0], line[1])
    print()

    print(cipher)

if __name__ == '__main__':
    main()
