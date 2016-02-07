from itertools import chain
import string

def main():
    cipher = ""
    cipher_dict = {}
    cipher_frequency = {}
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
        print("Frequencies of chars in Cipher[" + str(i) + "::"+ str(gcd) + "]")
        for line in sorted(cipher_frequency[i].items(), key=lambda x: x[1],
                           reverse=True):
            print(line[0], line[1])
        print()

    alphabet1 = '\'JKYLF' + 'Z M;UIPXS-T,OGDANCHRVWQB.*'
    alphabet2 = ', IHME'  + 'NCW;AFD.B*YRUKXL-GVTSQ\'*J*'
    alphabet3 = 'P BNWJ'  + 'CYVKF,OL;ATEHIZS.-\'RQUGDM*'
    alphabet4 = 'SM*JOL'  + ',QWBPVHYDGEINT\'R*ZF.XKAU_*'
    alphabet5 = '*.*MKI'  + 'ZUER-PVLXYB_W;GSFCT\'AJQOHN'

    cipher_alphabet = [alphabet1, alphabet2, alphabet3, alphabet4, alphabet5]

    shift = []
    for i, bet in enumerate(cipher_alphabet):
        shift.append(shift_alphabet(cipher[i::gcd], bet))

    print("".join(list(chain(*zip(*(shift))))))


def shift_alphabet(text, new_alphabet):
    full_alphabet = list('-\';,. ' + string.ascii_lowercase)
    new_alphabet = list(new_alphabet)

    text = list(text)
    new_text = list(text)

    for i, c in enumerate(new_alphabet):
        for j, c2 in enumerate(text):
            if(c2 == c):
                new_text[j] = full_alphabet[i]

    return new_text


if __name__ == '__main__':
    main()
