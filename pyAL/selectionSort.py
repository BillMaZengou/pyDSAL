def selection_sort(a_list):
    for slot in range(len(a_list)-1, 0, -1):
        position_of_max = 0
        for location in range(1, slot+1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location

        a_list[slot], a_list[position_of_max] = a_list[position_of_max], a_list[slot]

def main():
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()
