import time


class MergeSort:
    number_of_comparisons = 0

    @staticmethod
    def sort_ascending(array, key=lambda obj: obj):

        if len(array) == 1:
            return

        middle_index = len(array) // 2

        left = array[:middle_index]
        right = array[middle_index:]

        MergeSort.sort_ascending(left)
        MergeSort.sort_ascending(right)

        left_index, right_index, final_array_index = 0, 0, 0
        while left_index < len(left) and right_index < len(right):
            MergeSort.number_of_comparisons += 2
            if key(left[left_index]) < key(right[right_index]):
                MergeSort.number_of_comparisons += 1
                array[final_array_index] = left[left_index]
                left_index += 1

            else:
                array[final_array_index] = right[right_index]
                right_index += 1

            final_array_index += 1

        while left_index < len(left):
            MergeSort.number_of_comparisons += 1
            array[final_array_index] = left[left_index]
            final_array_index += 1
            left_index += 1

        while right_index < len(right):
            MergeSort.number_of_comparisons += 1
            array[final_array_index] = right[right_index]
            final_array_index += 1
            right_index += 1

        return f'Merge sort\n' \
               f'number of comparisons: {MergeSort.number_of_comparisons}\n' \
               f'sorted array: {array}'
