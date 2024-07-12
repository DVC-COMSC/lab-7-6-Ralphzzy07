
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    user_input = input("Enter multiple values separated by spaces: ")
    return list(map(int, user_input.split()))


def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """

    reverse_list = []
    while numbers:
        reverse_list.append(numbers.pop())
    return reverse_list


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
