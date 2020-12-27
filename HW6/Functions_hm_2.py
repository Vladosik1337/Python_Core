from math import sqrt


def main():
    enter_square = input("Enter what square you want: ")
    if "rect" in enter_square:
        def square_rectangle():
            """
            this function square_rectangle
            return square of a rectangle

            :return: s
            """
            a = int(input("Enter first side: "))
            b = int(input("Enter second side: "))
            s = (a+b) * 2
            return s
        print("Square_rectangle =",square_rectangle())
    elif "tria" in enter_square:
        def square_triangle():
            """
            this function square_rectangle
            return square of a triangle

            :return: s
            """
            a = int(input("Enter first side: "))
            b = int(input("Enter second side: "))
            c = int(input("Enter third side: "))
            p = (a + b + c) / 2
            s = sqrt(p * (p - a) * (p - b) * (p - c))
            return round(s, 2)
        print("Square_triangle =", square_triangle())
    else:
        def square_circle():
            """
            this function square_rectangle
            return square of a circle

            :return: s
            """
            r = int(input("Enter radius: "))
            PI = 3.14
            s = PI * (r ** 2)
            return s
        print("Square_circle =", square_circle())

main()
