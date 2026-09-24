import sys

def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        for arg in reversed(sys.argv[1:]):
            print(arg)

if __name__ == "__main__":
    main()