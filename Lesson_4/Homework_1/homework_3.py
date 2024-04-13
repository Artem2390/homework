def print_star():
    print('*', end='')


def print_space():
    print(' ', end='')


def print_newline():
    print()


height = 20

for i in range(height + 1):
    for j in range(i):
        print_star()
        print_space()
    print_newline()
