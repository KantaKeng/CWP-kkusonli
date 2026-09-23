try:
    user_input = input()
    print(user_input.swapcase())
except EOFError:
    pass