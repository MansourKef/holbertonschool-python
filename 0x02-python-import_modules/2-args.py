#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv)))
        count = 0
        for filearg in sys.argv:
            count = count + 1
            print("{}: {}".format(count, filearg))
