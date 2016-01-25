def main():
    cipher_dict = {}
    cipher_frequency = {}
    cipher = ""

    with open("ciphers/substitution_cipher.txt", "r") as cipher_file:
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

    # uncipher = '_' * len(cipher)
    uncipher = cipher

    # Space is most occuring in the englsih language so p->' '
    uncipher = replace(cipher, uncipher, 'p', ' ')
    # Then comes e so r->e
    uncipher = replace(cipher, uncipher, 'r', 'e')

    # I see a lot of 19e, so 19 is probably th, the is most occuring Trigram.
    uncipher = replace(cipher, uncipher, '1', 't')
    uncipher = replace(cipher, uncipher, '9', 'h')

    # See a Theze, so z->r is likely, fits frequencies
    uncipher = replace(cipher, uncipher, 'z', 'r')

    # See thlt, the;r, so l->a, ;->i, fits frequencies
    uncipher = replace(cipher, uncipher, 'l', 'a')
    uncipher = replace(cipher, uncipher, ';', 'i')

    # See ' 'i:' ', so :->n, fits frequencies
    uncipher = replace(cipher, uncipher, ':', 'n')

    # See everfthin-, so f->y, -->g fits frequencies
    uncipher = replace(cipher, uncipher, 'f', 'y')
    uncipher = replace(cipher, uncipher, '-', 'g')
    uncipher = replace(cipher, uncipher, 'v', 'v')

    # See htirring, so h->s fits frequencies
    uncipher = replace(cipher, uncipher, 'h', 's')

    # See g8es 8n, so 8->o fits frequencies
    uncipher = replace(cipher, uncipher, '8', 'o')

    # From here on words become pretty clear
    # Fix Raiyoay
    uncipher = replace(cipher, uncipher, 'o', 'w')
    uncipher = replace(cipher, uncipher, 'y', 'l')

    # Fix sinnessive
    uncipher = replace(cipher, uncipher, 'n', 'c')
    uncipher = replace(cipher, uncipher, 'i', 'u')

    # Fix a terri7le
    uncipher = replace(cipher, uncipher, '7', 'b')

    # Fix have acmuirew
    uncipher = replace(cipher, uncipher, 'm', 'q')
    uncipher = replace(cipher, uncipher, 'w', 'd')

    # Fix trans orts
    uncipher = replace(cipher, uncipher, ' ', 'p')

    # Fix oe
    uncipher = replace(cipher, uncipher, 'e', 'f')

    # six = six
    uncipher = replace(cipher, uncipher, 'x', 'x')

    # accosplishedd
    uncipher = replace(cipher, uncipher, 's', 'm')

    # citikens
    uncipher = replace(cipher, uncipher, 'k', 'z')

    # mantind
    uncipher = replace(cipher, uncipher, 't', 'k')

    # cromwellb
    uncipher = replace(cipher, uncipher, 'b', ':')

    # seed-time
    uncipher = replace(cipher, uncipher, 'a', '-')

    uncipher = replace(cipher, uncipher, 'c', ',')
    uncipher = replace(cipher, uncipher, 'd', '.')
    uncipher = replace(cipher, uncipher, 'q', ';')

    uncipher = replace(cipher, uncipher, ',', '1')
    uncipher = replace(cipher, uncipher, 'u', '7')
    uncipher = replace(cipher, uncipher, '.', '8')
    uncipher = replace(cipher, uncipher, 'g', '9')

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
