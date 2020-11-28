"""
input data examples
"""
hamster_in_1 = [1, 4, (5, 0), (2, 2), (1, 4), (5, 1)]
hamster_in_2 = [7, 3, (1, 2), (2, 4), (2, 2)]
hamster_in_3 = [2, 2, (1, 1), (2, 0)]
hamster_in_4 = [6, 4, (1, 1), (1, 2), (3, 2), (1, 2)]
hamster_in_5 = [4, 2, (3, 1), (1, 0)]


def get_hunger(hamster_in):
    hunger = []
    for hamster_index in range(2, len(hamster_in)):
        hunger.append(hamster_in[hamster_index][0])
    return hunger


def max_count_if_few_hamsters(hamster_in):
    greediest_hamster = None
    greediest_hamster_hunger, hamsters_to_feed_hunger = 0, 0
    for hamster_index in range(2, len(hamster_in)):
        current_hamster_hunger = hamster_in[hamster_index][0] + hamster_in[hamster_index][1] * (len(hamster_in) - 3)
        hamsters_to_feed_hunger += current_hamster_hunger
        if greediest_hamster_hunger < current_hamster_hunger:
            greediest_hamster_hunger = current_hamster_hunger
            greediest_hamster = hamster_index
    if hamsters_to_feed_hunger <= hamster_in[0]:
        return len(hamster_in) - 2
    else:
        hamster_in.pop(greediest_hamster)
        return max_count_if_few_hamsters(hamster_in)


def max_hamsters_count_with_edge_case(hamster_in):
    """
    Finds number of hamsters that can be fed this day considering task conditions
    >>> max_hamsters_count_with_edge_case(hamster_in_1)
    1

    >>> max_hamsters_count_with_edge_case(hamster_in_2)
    2

    >>> max_hamsters_count_with_edge_case(hamster_in_3)
    1

    >>> max_hamsters_count_with_edge_case(hamster_in_4)
    2

    >>> max_hamsters_count_with_edge_case(hamster_in_5)
    1
    """
    if hamster_in[1] == 1 and hamster_in[2][0] <= hamster_in[0]:
        return 1
    elif hamster_in[1] == 1 and hamster_in[2][0] >= hamster_in[0]:
        return 0

    hunger = get_hunger(hamster_in)
    result = max_count_if_few_hamsters(hamster_in)
    if result != 0:
        return result
    else:
        for hamster_hunger in hunger:
            if hamster_in[0] >= hamster_hunger:
                return 1
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)