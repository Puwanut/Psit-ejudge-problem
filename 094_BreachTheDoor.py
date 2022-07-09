"""BreachTheDoor"""
def main(text):
    """print word in paragraph that more than 6 characters"""
    wordlist = text.split()
    for word in wordlist:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, "")
        if len(word) > 6:
            print(word, end=" ")
main(input())
