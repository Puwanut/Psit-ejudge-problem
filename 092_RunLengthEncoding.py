"""Run Length Encoding"""
def main(text):
    """convert text to encoded text"""
    memory = text[0]
    count = 0
    for char in text+"0":
        if memory == char:
            count += 1
        else:#เมื่อ char กลายเป็นตัวอักษรใหม่
            print(str(count) + memory, end="")
            memory = char
            count = 1
main(input())
