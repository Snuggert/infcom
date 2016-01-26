def main():
    cipher = ""

    with open("ciphers/polyalphabetic_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()

    qbry = []
    skol = []
    for i in range(0, len(cipher)):
        if(cipher[i:i + 4] == 'QBRY'):
            qbry.append(i)
        elif(cipher[i:i + 4] == 'SKOL'):
            skol.append(i)
    print(qbry)
    print(skol)

    # Wolfram GCD, means alphabet repeats every 5 characters
    gcd = 5

    cipher_dict = [{} for i in range(0, gcd)]

    for i in range(0, gcd):
        for c in cipher[i::gcd]:
            if(c in cipher_dict[i].keys()):
                cipher_dict[i][c] += 1
            else:
                cipher_dict[i][c] = 1

    print("Number of different chars: ",
          [len(cipher_dict[i]) for i in range(0, len(cipher_dict))])

    cipher_frequency = [{} for i in range(0, gcd)]
    for i in range(0, gcd):
        for c in cipher_dict[i]:
            cipher_frequency[i][c] = (cipher_dict[i][c] /
                                      float(len(cipher[i::gcd]))) * 100

    for i in range(0, gcd):
        print("Frequencies of chars in Cipher[" + str(i) + "::5]")
        for line in sorted(cipher_frequency[i].items(), key=lambda x: x[1],
                           reverse=True):
            print(line[0], line[1])
        print()

    # uncipher = '_' * len(cipher)
    # uncipher = cipher
    print(cipher)


def replace(string, otherstring, orig, new):
    char_indices = [i for i, c in enumerate(list(string)) if c == orig]
    for i in char_indices:
        otherstring = list(otherstring)
        otherstring[i] = new
        otherstring = "".join(otherstring)
    return otherstring


if __name__ == '__main__':
    main()
