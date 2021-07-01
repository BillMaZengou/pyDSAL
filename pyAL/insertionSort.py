def insertion_sort(a_list):
    for idx in range(1, len(a_list)):
        current_value = a_list[idx]
        pos = idx

        while pos > 0 and a_list[pos-1] > current_value:
            a_list[pos] = a_list[pos-1]
            pos -= 1

        a_list[pos] = current_value

def main():
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()
