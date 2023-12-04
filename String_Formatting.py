def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal_value = str(i)
        octal_value = oct(i)[2:]
        hexadecimal_value = hex(i)[2:].upper()
        binary_value = bin(i)[2:]
        print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(decimal_value, octal_value,
                                                                       hexadecimal_value, binary_value, width=width))

n = int(input())
print_formatted(n)
