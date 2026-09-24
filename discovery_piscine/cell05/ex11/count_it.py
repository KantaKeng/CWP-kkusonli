#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        print(f"parameters: {len(sys.argv) - 1}")
        for arg in sys.argv[1:]:
            print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    main()