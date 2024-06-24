#!/usr/bin/python3

while True:
    cpu_model = input("Intel core i 3|5|7|9 or 0 to leave : ")
    cpu_model = int(cpu_model)

    match cpu_model:
        case 0:
            break
        case 3:
            print("Intel core i3", end="\n\n")
        case 5:
            print("Intel core i5", end="\n\n")
        case 7:
            print("Intel core i7", end="\n\n")
        case 9:
            print("Intel core i9", end="\n\n")
        case _:
            print("Usage: 3|5|7|9 or 0", end="\n\n")
