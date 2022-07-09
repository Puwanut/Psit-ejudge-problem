"""Fizz Buzz"""
def main(num):
    """loop num and print according condition"""
    for i in range(1, num+1):
        if i%3 == 0 and i%5 == 0:
            print("Fizz Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
main(int(input()))
