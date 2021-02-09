from random import randint

def generate_matrix():
    return [[randint(10, 50) for i in range(10)] for j in range(10)]


def check_rows(matrix, num):
    index_lst = []

    for ind, el in enumerate(matrix):
        if num in el:
            index_lst.append(ind)
    return index_lst


def check_columns(matrix, num):
    column_to_row_lst = [[] for i in range(10)]
    
    for ind, el in enumerate(matrix):
        counter = 0
        for subind, subel in enumerate(el):
            if subind == counter:
                column_to_row_lst[counter].append(subel)
            counter += 1
    return check_rows(column_to_row_lst, num)


def get_index(num):
    matrix = generate_matrix()

    rows = " ".join(list(map(str, check_rows(matrix, num))))
    columns = " ".join(list(map(str, check_columns(matrix, num))))

    data = (f"Number range (10, 50): {num}\n"
            f"Rows (index): {rows}\n"
            f"Columns (index): {columns}")

    for el in matrix:
        print(" ".join(list(map(str, el))))
    print()

    return data