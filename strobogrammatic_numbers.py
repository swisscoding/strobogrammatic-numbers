#!/usr/local/bin/python3
# Edited by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Strobogrammatic numbers | ----\n", fg("red")))

# functions
def strobogrammatic_numbers(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = execute(n, n)
    return result

def execute(n, length):
    if n == 0:
        return [""]
    elif n == 1:
        return ["1", "0", "8"]

    middles = execute(n - 2, length)
    output = []

    for middle in middles:
        if n != length:
            output.append("0" + middle + "0")

        output.append("8" + middle + "8")
        output.append("1" + middle + "1")
        output.append("9" + middle + "6")
        output.append("6" + middle + "9")

    return output

if __name__ == "__main__":
    try:
        # user interaction
        n = int(input("Length of strobogrammatic numbers: "))

        # output
        print(stylize(f"\nStrobogrammatic numbers with length of {n}:", fg("red")))
        print(strobogrammatic_numbers(n))
        print()
    except:
        exit("\nInvalid Input\n")
