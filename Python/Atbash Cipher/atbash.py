lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encode(phrase):
    result = []
    for i in phrase:
        if i.isupper():
            result.append(upper_alphabet[::-1][upper_alphabet.index(i)])
        if i.islower():
            result.append(lower_alphabet[::-1][lower_alphabet.index(i)])
        else:
            result.append(i)
    print(''.join(result))

encode("Apple 25 appLE")
