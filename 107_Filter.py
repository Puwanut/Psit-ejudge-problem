"""Filter"""
import json
def passed_student(sidpoint_dict, minpoint):
    """Show students with passing scores"""
    student_list = []
    for sid in sidpoint_dict:
        if sidpoint_dict[sid] >= minpoint:
            student_list.append(sid)
    student_list.sort()
    if len(student_list) == 0:
        print("Nope")
    else:
        for sid in student_list:
            point = sidpoint_dict[sid]
            print("%s\t%.2f"%(sid, point))
passed_student(json.loads(input()), float(input()))
