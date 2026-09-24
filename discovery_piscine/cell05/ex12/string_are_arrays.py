import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        text = sys.argv[1]
        count = text.count("z")
        if count == 0:
            print("none")
        else:
            print("z" * count)

if __name__ == "__main__":
    main()