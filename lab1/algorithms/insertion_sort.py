class InsertionSort:
    number_of_comparisons = 0
    number_of_swaps = 0

    @staticmethod
    def descending_sort(array, key=lambda obj: obj):
        for i in range(1, len(array)):
            current = i
            while current > 0 and key(array[current - 1]) < key(array[current]):
                InsertionSort.number_of_comparisons += 2
                array[current - 1], array[current] = array[current], array[current - 1]
                InsertionSort.number_of_swaps += 1
                current -= 1

        return f'Insertion sort\n' \
               f'number of comparisons: {InsertionSort.number_of_comparisons}\n' \
               f'number of swaps: {InsertionSort.number_of_swaps},\n' \
               f'sorted array: {array}'
