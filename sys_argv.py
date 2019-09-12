import sys

if __name__ == "__main__":
    print("number of args: {}".format(len(sys.argv)))
    for arg in sys.argv:
        print(arg)
