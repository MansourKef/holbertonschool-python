#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Total = 0
    for filearg in sys.argv[1:]:
        Total += int(filearg)
    print(Total)
