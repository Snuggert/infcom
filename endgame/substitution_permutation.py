def main():
    cipher_dict = {}
    cipher_frequency = {}
    cipher = ""

    with open("ciphers/permutation_and_substitution_cipher.txt", "r") as \
            cipher_file:
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

    # uncipher = '_' * len(cipher)
    uncipher = cipher

    # Space is most occuring in the englsih language so p->' '
    uncipher = replace(cipher, uncipher, 'J', ' ')
    # Then comes et so i->e z->t
    uncipher = replace(cipher, uncipher, 'I', 'e')
    uncipher = replace(cipher, uncipher, 'Z', 't')

    listuncipher = list(uncipher)
    list2uncipher = list(uncipher)
    for i in range(0, len(uncipher), 5):
        listuncipher[i] = list2uncipher[i + 4]
        listuncipher[i + 1] = list2uncipher[i + 3]
        listuncipher[i + 2] = list2uncipher[i + 1]
        listuncipher[i + 3] = list2uncipher[i]
        listuncipher[i + 4] = list2uncipher[i + 2]
    uncipher = "".join(listuncipher)
    cipher = uncipher

    # Fill tTe
    uncipher = replace(cipher, uncipher, 'T', 'h')

    # Fill th?t
    uncipher = replace(cipher, uncipher, '?', 'a')

    # See UQ, behind th and begin h
    uncipher = replace(cipher, uncipher, 'U', 'i')
    uncipher = replace(cipher, uncipher, 'Q', 's')

    # Fill t'
    uncipher = replace(cipher, uncipher, '\'', 'o')

    # See aF" a lot. and is a common trigram.
    uncipher = replace(cipher, uncipher, 'F', 'n')
    uncipher = replace(cipher, uncipher, '\"', 'd')

    # See this Das && DithoOt
    uncipher = replace(cipher, uncipher, 'D', 'w')
    uncipher = replace(cipher, uncipher, 'O', 'u')

    # See waitinL
    uncipher = replace(cipher, uncipher, 'L', 'g')

    # # From here on words become pretty clear
    uncipher = replace(cipher, uncipher, 'G', 'q')
    uncipher = replace(cipher, uncipher, '.', 'f')
    uncipher = replace(cipher, uncipher, 'S', 'c')
    uncipher = replace(cipher, uncipher, '!', 'r')
    uncipher = replace(cipher, uncipher, '-', 'y')
    uncipher = replace(cipher, uncipher, ',', 'z')
    uncipher = replace(cipher, uncipher, 'H', 'j')

    # See father;s
    uncipher = replace(cipher, uncipher, ';', '\'')

    uncipher = replace(cipher, uncipher, 'A', 'm')
    uncipher = replace(cipher, uncipher, 'K', 'b')
    uncipher = replace(cipher, uncipher, 'X', 'l')
    uncipher = replace(cipher, uncipher, 'B', 'v')
    uncipher = replace(cipher, uncipher, 'P', 'k')
    uncipher = replace(cipher, uncipher, 'V', 'p')
    uncipher = replace(cipher, uncipher, 'R', 'x')

    uncipher = replace(cipher, uncipher, 'Y', '-')
    uncipher = replace(cipher, uncipher, 'W', '.')
    uncipher = replace(cipher, uncipher, 'E', ';')
    uncipher = replace(cipher, uncipher, 'M', ',')
    uncipher = replace(cipher, uncipher, 'C', '\"')
    uncipher = replace(cipher, uncipher, 'N', '?')

    print(uncipher)


def replace(string, otherstring, orig, new):
    char_indices = [i for i, c in enumerate(list(string)) if c == orig]
    for i in char_indices:
        otherstring = list(otherstring)
        otherstring[i] = new
        otherstring = "".join(otherstring)
    return otherstring


if __name__ == '__main__':
    main()
