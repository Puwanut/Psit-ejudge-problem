"""LetterFrequency"""
def main(sentence, most_char, most_count):
    """print the most used character"""
    charlist = []
    for char in sentence:
        if char not in charlist and char.isalpha():
            charlist.append(char)
    for char in charlist:
        count = sentence.count(char)
        if count > most_count:
            most_count = count
            most_char = char
    print(most_char)
main(input().lower(), "", 0)
