from math import pow, pi
if __name__ != "__main__":
    def square_rectangle(a, b):
        """
        this function square_rectangle
        return square of a rectangle

        :return: s
        """
        s = a * b
        return s



    def square_triangle(h, a):
        """
        this function square_rectangle
        return square of a triangle

        :return: s
        """
        s = 0.5 * h * a
        return round(s, 2)

    def square_circle(r):
        """
        this function square_rectangle
        return square of a circle

        :return: s
        """
        s = pi * pow(r, 2)
        return round(s,3)


