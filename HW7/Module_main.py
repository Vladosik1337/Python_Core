import Module_square

enter_square = input("Enter what square you want: \n'rect' = 'recatngle'\n'tria' = 'triangle'\n'circ' = 'circle': ")
if "rect" in enter_square:
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    square = Module_square.square_rectangle(a, b)
    print(square)
elif "tria" in enter_square:
    a = int(input("Enter Side: "))
    h = int(input("Enter Height"))
    square = Module_square.square_triangle(a, h)
    print(square)
else:
    r = int(input("Enter radius: "))
    square = Module_square.square_circle(r)
    print(square)