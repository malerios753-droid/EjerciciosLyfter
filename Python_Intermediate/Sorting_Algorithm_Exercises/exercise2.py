def bubble_sort_reverse(list_to_sort):
    n = len(list_to_sort)

    for outer_index in range(n - 1):
        has_made_changes = False

        for index in range(n - 1, outer_index, -1):
            current_element = list_to_sort[index]
            left_element = list_to_sort[index - 1]

            if current_element < left_element:
                list_to_sort[index] = left_element
                list_to_sort[index - 1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return list_to_sort

    return list_to_sort



if __name__ == "__main__":
    numbers = [18, -11, 68, 7, 32, 53, -2]
    print("Original:", numbers)
    bubble_sort_reverse(numbers)
    print("Ordenada (derecha a izquierda):", numbers)

    empty_list = []
    single_item = [28]
    already_sorted = [1, 2, 3, 4, 5]

    print('Vacia:', bubble_sort_reverse(empty_list))
    print("Un elemnto:", bubble_sort_reverse(single_item))
    print("Ya ordenada", bubble_sort_reverse(already_sorted))
