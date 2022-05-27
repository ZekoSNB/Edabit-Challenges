lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
reversed_lower_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
reversed_upper_alphabet = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

coded_phrase = []
index_list = []


def encode(phrase):
    phrase_list = list(phrase)
    for letter in phrase_list:
        if letter.islower():
            for index in range(len(lower_alphabet)):
                if lower_alphabet[index] == letter:
                    index_list.append(index)
                    break
        elif letter.isupper():
            for index in range(len(upper_alphabet)):
                if upper_alphabet[index] == letter:
                    index_list.append(index)
                    break

    lower_alphabet.reverse()
    for i in index_list:
        coded_phrase.append(lower_alphabet[i])
    print(''.join(coded_phrase))

encode("Apple")
