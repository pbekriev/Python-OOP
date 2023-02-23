def get_pattern_data(data):
    pattern, size = data

    if pattern == 'Rombus':
        for x in range(size):
            space_data = size - x - 1
            stars_data = x + 1
            print_pattern_data(space_data, stars_data)

        for x in range(size - 2, -1, -1):
            space_data = size - x - 1
            stars_data = x + 1
            print_pattern_data(space_data, stars_data)

    elif pattern == 'Triangle':
        for x in range(size):
            stars_data = x + 1
            print_pattern_data(0, stars_data)

    elif pattern == 'Square':
        for x in range(size):
            print_pattern_data(0, size)


def print_pattern_data(space_data, stars_data):
    print(' ' * space_data + '*' * stars_data)


def choise_pattern():
    pattern = input('Choice type of pattern ->\n- Triangle\n- Rombus\n- Square\nPattern choise: ')
    pattern_size = int(input())
    return pattern, pattern_size


get_pattern_data(choise_pattern())
