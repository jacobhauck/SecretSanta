import itertools
import random


def is_illegal(permutation, i_illegal):
    for i, j in enumerate(permutation):
        if i == j:
            return True

        if j in i_illegal[i]:
            return True

    return False


def brute_force(names, illegal):
    index = {name: i for i, name in enumerate(names)}
    i_illegal = []
    for name in names:
        if name in illegal:
            i_illegal.append(frozenset(index[n] for n in illegal[name]))
        else:
            i_illegal.append(frozenset())

    valid = []
    for p in itertools.permutations(range(len(names))):
        if not is_illegal(p, i_illegal):
            valid.append(p)

    return {names[i]: names[j] for i, j in enumerate(random.choice(valid))}
