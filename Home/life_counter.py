import copy


def count_neighbours(array, row_index, column_index):
    # validate available rows around certain point
    if row_index == 0:
        rows_to_check = [row_index, row_index + 1]
    elif row_index == len(array) - 1:
        rows_to_check = [row_index - 1, row_index]
    else:
        rows_to_check = [row_index - 1, row_index, row_index + 1]

    # validate available columns around certain point
    if column_index == 0:
        columns_to_check = [column_index, column_index + 1]
    elif column_index == len(array[0]) - 1:
        columns_to_check = [column_index - 1, column_index]
    else:
        columns_to_check = [column_index - 1, column_index, column_index + 1]

    # count alive cells around point
    counter = 0
    for row in rows_to_check:
        for col in columns_to_check:
            if row == row_index and col == column_index:
                continue
            if array[row][col] == 1:
                counter += 1
    return counter


def life_tick(array):
    array = list(array)
    array = [list(row) for row in array]

    # expand if there is potential to grow:
    if any(array[-1]):  # last row
        array.append([0] * len(array[-1]))
    if any(array[0]):  # first row
        array.insert(0, [0] * len(array[0]))
    first_column = [val[0] for val in array]
    if any(first_column):
        for index in range(len(array)):
            array[index].insert(0, 0)
    last_column = [val[-1] for val in array]
    if any(last_column):
        for index in range(len(array)):
            array[index].append(0)

    # create a copy of existing array
    new_array = copy.deepcopy(array)

    # kill or resurrect cells
    for row_index, row in enumerate(array):
        for column_index, column in enumerate(row):
            neighbours = count_neighbours(array, row_index, column_index)
            if column == 0:  # if cell is dead
                if neighbours == 3:
                    new_array[row_index][column_index] = 1  # make it alive
            else: # if cell is alive
                if neighbours < 2:  # underpopulation
                    new_array[row_index][column_index] = 0  # make it dead
                elif neighbours > 3:  # overpopulation
                    new_array[row_index][column_index] = 0  # make it dead
    return new_array


def life_counter(array, number):
    for i in range(number):
        array = life_tick(array)
        counter = 0
        for row in array:
            for col in row:
                if col == 1:
                    counter += 1
    return counter

