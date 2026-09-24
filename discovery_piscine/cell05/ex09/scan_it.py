import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        keyword = sys.argv[1]
        text = sys.argv[2]
        matches = re.findall(keyword, text)
        if len(matches) == 0:
            print("none")
        else:
            print(len(matches))

if __name__ == "__main__":
    main()