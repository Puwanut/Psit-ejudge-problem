"""Run Length Decoding"""
def main(code, amount):
    """decode encoded text to text"""
    for i in code:
        if i.isdigit():#เมื่อ i เป็นตัวเลข
            amount += i
        else:#เมื่อ i เป็นตัวอักษร
            print(i*int(amount), end="")
            amount = ""
main(input(), "")
