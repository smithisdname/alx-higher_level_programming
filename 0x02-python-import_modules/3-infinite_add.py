#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_inp = len(argv)
    total = 0

    for i in range(1, num_inp):
        total += int(argv[i])
    print(total)
