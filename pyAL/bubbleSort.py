def bubble_sort(a_list):
    for rest_number in range(len(a_list) - 1, 0, -1):
        for i in range(rest_number):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

def short_bubble_sort(a_list):
    exchanges = True
    rest_number = len(a_list) - 1
    while rest_number > 0 and exchanges:
        exchanges = False
        for i in range(rest_number):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        rest_number -= 1

def main():
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(test_list)
    print(test_list)
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    short_bubble_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()
