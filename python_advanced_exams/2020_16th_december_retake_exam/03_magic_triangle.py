#   Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a
#   magic triangle which follows those rules:
#   •	We start with this simple triangle [[1], [1, 1]]
#   •	We generate the next rows until we reach n amount of rows
#   •	Each number in each row is equal to the sum of the two numbers right above it in the triangle
#   •	If the current number has no neighbor to the upper left/right, we just take the existing neighbor
#   After you create the magic triangle, return it as a multidimensional list.

def get_magic_triangle(num):
    triangle = []
    for row in range(1, num + 1):
        if row == 1:
            triangle.append([1])
        elif row == 2:
            triangle.append([1, 1])
        else:
            current_row = [1]
            for i in range(len(triangle[row - 2]) - 1):
                current_row.append(triangle[row - 2][i] + triangle[row - 2][i + 1])
            current_row.append(1)
            triangle.append(current_row)

    return triangle


print(get_magic_triangle(4))