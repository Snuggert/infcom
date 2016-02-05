def main():
    cipher_dict = {}
    cipher_frequency = {}
    cipher = ""

    with open("ciphers/substitution_cipher.txt", "r") as cipher_file:
        cipher = cipher_file.read()

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

    uncipher = '_' * len(cipher)
    # uncipher = cipher

    # Space is most occuring in the englsih language so p->' '
    uncipher = replace(cipher, uncipher, 'P', ' ')
    # Then comes e so r->e
    uncipher = replace(cipher, uncipher, 'R', 'e')

    # I see a lot of 19e, so 19 is probably th, the is most occuring Trigram.
    uncipher = replace(cipher, uncipher, '1', 't')
    uncipher = replace(cipher, uncipher, '9', 'h')

    # See a Theze, so z->r is likely, fits frequencies
    uncipher = replace(cipher, uncipher, 'Z', 'r')

    # See thlt, the;r, so l->a, ;->i, fits frequencies
    uncipher = replace(cipher, uncipher, 'L', 'a')
    uncipher = replace(cipher, uncipher, ';', 'i')

    # See ' 'i:' ', so :->n, fits frequencies
    uncipher = replace(cipher, uncipher, ':', 'n')

    # See everfthin-, so f->y, -->g fits frequencies
    uncipher = replace(cipher, uncipher, 'F', 'y')
    uncipher = replace(cipher, uncipher, '-', 'g')
    uncipher = replace(cipher, uncipher, 'V', 'v')

    # See htirring, so h->s fits frequencies
    uncipher = replace(cipher, uncipher, 'H', 's')

    # See g8es 8n, so 8->o fits frequencies
    uncipher = replace(cipher, uncipher, '8', 'o')

    # From here on words become pretty clear
    # Fix Raiyoay
    uncipher = replace(cipher, uncipher, 'O', 'w')
    uncipher = replace(cipher, uncipher, 'Y', 'l')

    # Fix sinnessive
    uncipher = replace(cipher, uncipher, 'N', 'c')
    uncipher = replace(cipher, uncipher, 'I', 'u')

    # Fix a terri7le
    uncipher = replace(cipher, uncipher, '7', 'b')

    # Fix have acmuirew
    uncipher = replace(cipher, uncipher, 'M', 'q')
    uncipher = replace(cipher, uncipher, 'W', 'd')

    # Fix trans orts
    uncipher = replace(cipher, uncipher, ' ', 'p')

    # Fix oe
    uncipher = replace(cipher, uncipher, 'E', 'f')

    # six = six
    uncipher = replace(cipher, uncipher, 'X', 'x')

    # accosplishedd
    uncipher = replace(cipher, uncipher, 'S', 'm')

    # citikens
    uncipher = replace(cipher, uncipher, 'K', 'z')

    # mantind
    uncipher = replace(cipher, uncipher, 'T', 'k')

    # cromwellb
    uncipher = replace(cipher, uncipher, 'B', ':')

    # seed-time
    uncipher = replace(cipher, uncipher, 'A', '-')

    uncipher = replace(cipher, uncipher, 'C', ',')
    uncipher = replace(cipher, uncipher, 'D', '.')
    uncipher = replace(cipher, uncipher, 'Q', ';')

    uncipher = replace(cipher, uncipher, ',', '1')
    uncipher = replace(cipher, uncipher, 'U', '7')
    uncipher = replace(cipher, uncipher, '.', '8')
    uncipher = replace(cipher, uncipher, 'G', '9')

    print("BLACKWOOD'S MAGAZINE, Jan. 1845: ", uncipher)
    # print(cipher)


def replace(string, otherstring, orig, new):
    char_indices = [i for i, c in enumerate(list(string)) if c == orig]
    for i in char_indices:
        otherstring = list(otherstring)
        otherstring[i] = new
        otherstring = "".join(otherstring)
    return otherstring


if __name__ == '__main__':
    main()
