"""HelloWorldComeBack"""
def main(word):
    """hello with same language of 'word'"""
    if ord("A") <= ord(word[0]) <= ord("z"):
        print("Hello %s."%word)
    else:
        print("สวัสดี %s"%word)
main(input())
