def shell_sort(a_list):
    sub_list_count = len(a_list) // 2
    while sub_list_count > 0:
        for start_pos in range(sub_list_count):
            gap_insertion_sort(a_list, start_pos, sub_list_count)

        print("After increments of size", sub_list_count, "The list is", a_list)

        sub_list_count //= 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position-gap] > current_value:
            a_list[position] = a_list[position-gap]
            position -= gap

        a_list[position] = current_value

def main():
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()
