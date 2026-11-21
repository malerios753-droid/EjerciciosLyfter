def bubble_sort(list_to_sort):
    n = len(list_to_sort)

    for outer_index in range(n - 1):
        has_made_changes = False

        for index in range(n - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return list_to_sort

    return list_to_sort


if __name__ == "__main__":
    numbers = [18, -11, 68, 7, 32, 53, -2]
    print("Original:", numbers)
    bubble_sort(numbers)
    print("Ordenada:", numbers)

    empty_list = []
    single_item = [42]
    already_sorted = [1, 2, 3, 4, 5]

    print("Vacia:", bubble_sort(empty_list))
    print("Un elemnto:", bubble_sort(single_item))
    print("Ya ordenada", bubble_sort(already_sorted))