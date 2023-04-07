def print_table(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]:>3}', end=' ')
        
        print()


def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix: list[list] = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = operation(j + 1, i + 1)
    
    print_table(matrix)


print_operation_table(lambda x, y: x * y)