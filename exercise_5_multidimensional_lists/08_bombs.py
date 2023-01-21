#   You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a
#   new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single
#   space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
#   On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes,
#   it deals damage equal to its integer value to all the surrounding cells (in every direction and in all diagonals).
#   One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or
#   below, it dies. Dead cells can't explode.
#   You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells
#   (including the dead ones).
#   Input
#   •	On the first line, you are given the integer N - the size of the square matrix.
#   •	The following N lines hold each column's values - N numbers separated by a space.
#   •	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
#   Output
#   •	On the first line, you need to print the count of all alive cells in the format:
#       "Alive cells: {alive_cells}"
#   •	On the second line, you need to print the sum of all alive cells in the format:
#       "Sum: {sum_of_cells}"
#   •	In the end, print the matrix. A space must separate the cells.
#   Constraints
#   •	The size of the matrix will be between [0…1000].
#   •	The bomb coordinates will always be in the matrix.
#   •	The bomb's values will always be greater than 0.
#   •	The integers of the matrix will be in the range [1…10000].

rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
bomb_coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, -1),  # top_left
    (-1, 1),   # top_right
    (1, -1),   # down_left
    (1, 1),    # down_right
    (0, 0),    # bomb_location
)

for row, column in bomb_coordinates:
    if matrix[row][column] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, column + y

        if 0 <= r < rows and 0 <= c < rows:
            matrix[r][c] -= matrix[row][column] if matrix[r][c] > 0 else 0

alive_cells = 0
sum_of_alive_cells = 0

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            sum_of_alive_cells += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")

for row in matrix:
    print(*row)



