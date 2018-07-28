# A simple program illustrating chaotic behaviour
import random


def main():
    print("This program illustrates a chaotic function")
    x = float((input("Enter a number between 0 and 1: ")))
    if 0 < x < 1:
        for i in range(10):
            x = random.randint(0, 10) * x * (1-x)
            print(x)
    else:
        print("Please enter a number BETWEEN 0 and 1")


if __name__ == '__main__':
    main()

