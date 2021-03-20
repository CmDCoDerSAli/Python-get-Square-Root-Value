# math module is imported
import math


class Sqrt():

    def __init__(self, number):
        self.number = number

    # square root is calculated using the find_sqrt() function
    def find_sqrt(self):

        # Negative number is checked
        if self.number < 0:
            print("Square Root exist for positive values")
        else:
            print("The square root is ", math.sqrt(self.number))


def main():
    # take value from user
    number = int(input("Enter the number: "))
    # Instance is created for class Sqrt
    # Parameter "number" is passed
    obj_Sqrt = Sqrt(number)
    obj_Sqrt.find_sqrt()


# Main function is checked
if __name__ == "__main__":
    main()

