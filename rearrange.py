import sys
import random


def main(arr):
    """Shuffles the input

    Params: arr - array of strings
    list -> string
    """
    shuffle(arr)
    return ' '.join(str(x) for x in arr)


def shuffle(array):
    """In place shuffling algorithm

    Params: array - list to shuffle
    list -> ()
    """
    for i in range(len(array)):
        j = random.randint(0, len(array)-1)
        array[i] = array[j]

if __name__ == "__main__":
    result = main(sys.argv[1:])
    print(result)
