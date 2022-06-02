lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

coded_phrase = []
index_list = []


def encode(phrase):
    phrase_list = list(phrase)
    for letter in phrase_list:
        if letter.isalpha():
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
        else:
            index_list.append(letter)
    print(index_list)
    lower_alphabet.reverse()
    upper_alphabet.reverse()
    for i in range(len(index_list)):
        if phrase_list[i].isalpha:
            if phrase_list[i].islower():
                coded_phrase.append(lower_alphabet[index_list[i]])
            if phrase_list[i].isupper():
                coded_phrase.append(upper_alphabet[index_list[i]])
        else:
            coded_phrase.append(phrase_list[i])
    print(''.join(coded_phrase))
encode("Apple 25 appLE")
