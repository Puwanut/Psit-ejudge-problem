"""AndAgain"""
def main(sentence):
    """Show words with 2 or more vowels"""
    countvowel = 0
    wordlist = sentence.split()
    showlist = []
    for word in wordlist:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, "")
            if char.lower() in "a e i o u":
                countvowel += 1
        if countvowel >= 2:
            showlist.append(word)
        countvowel = 0
    showlist.sort()
    if showlist == []:
        print("Nope")
    else:
        print(*showlist, sep="\n")
main(input())
