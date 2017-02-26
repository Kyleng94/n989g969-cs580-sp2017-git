# This program takes a number and finds the square root. It iterates through 10 numbers to find the square root.
#
# Kyle Nguyen
# N989G969
# Program 1

def main():
    x = input("Enter the number to find the square root of: ")
    square = x

    if x < 0:
        print("You have input an invalid number.")
        return

    print("Approximate Square Root: ")

    for i in range(10):
        x = ((x+(float(square)/x))/2)
        print(x)

    print "After 10 iterations, the approximate square root is", x
    print "The square of this number is",square

main()
