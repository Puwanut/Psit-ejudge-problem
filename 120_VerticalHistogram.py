"""VerticalHistogram"""
def show_charchart(text):
    """show Character frequency chart"""
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0)+1
    char_list = sorted(char_dict, key=str.swapcase)
    for i in range(max(char_dict.values()), 0, -1):
        print("%03d"%i, end=" ")
        for char in char_list:
            if i <= char_dict[char]:
                print("*", end=" ")
                char_dict[char] -= 1
            else:
                print(" ", end=" ")
        print()
    print("   ", *char_list)
show_charchart(input())
