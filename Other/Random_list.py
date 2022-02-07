import random


def random_list(length):
    gen_list = []
    for i in range(0, length):
        gen_list.append(random.randint(0, 100))

    return gen_list
