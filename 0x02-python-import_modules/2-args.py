#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    # arg_len = len(argv) - 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv) - 1, argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
