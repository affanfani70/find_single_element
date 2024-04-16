# [1,1,2,2,3,3,4,5,5,6,6]
# find the single element from the arr
# conditions: cannot take XOR, Cannot use dic/frequence, cannot use single iterate


def find_single_element(arr: list) -> list:
    left = 0
    right = len(arr) - 1
    # print('len', right)

    while left < right:
        # print('right=',right, 'left=',left, end='')
        mid = (left + right) // 2
        # print('mid=',mid, end='')
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
                # print("if1", left,  end='')
            else:
                right = mid
                # print("else1",right, end='')

        else:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
                # print("if2",left, end='')
            else:
                right = mid
                # print("else2",right, end='')
        # print()

    return arr[left]


if __name__ == "__main__":
    arr: list = [1, 1, 2, 2, 3, 3, 4, 4, 5,5, 6]
    element = find_single_element(arr)
    print(element)
