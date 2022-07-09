"""Classify"""
def main():
    """show student information"""
    stuid_list = []
    stuid_dict = {}
    while True:
        stuid = input()
        if stuid == "END":
            break
        stuid_list.append(stuid[:4])
    for stuid in stuid_list:
        stuid_dict[stuid] = stuid_dict.get(stuid, 0) + 1
    key_list = sorted(stuid_dict.keys())
    year_old = ""
    for key in key_list:
        if key[:2] != year_old:
            year_old = key[:2]
            year = key[:2]
        else:
            year = "--"
        print(year, int(key[2:4]), stuid_dict.get(key))
main()
