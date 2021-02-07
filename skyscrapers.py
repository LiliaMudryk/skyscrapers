"""
This module will allow you to check whether there is a winning combination
on the board in skyscrapers game.
"""
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    f_open = open(path,mode = "r",encoding="UTF-8")
    lines_lst = []
    for line in f_open:
        line = line.strip()
        lines_lst.append(line)


    return lines_lst


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    visibility = True
    visible = 1
    modified_row = input_line[1:-1]
    last_largest = int(modified_row[0])
    for number in modified_row:
        if int(number) > last_largest:
            last_largest = int(number)
            if int(number)>=last_largest :
                visible+=1
    if visible != pivot:
        visibility = False

    return visibility


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*',\
 '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    finished = True
    for i in board:
        if "?" in i:
            finished = False
            break
    return finished




def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    uniqueness = True
    for i,row in enumerate(board):
        modified_row = row[1:len(board)-1]
        if i not in (0, len(board) - 1):
            for j,number in enumerate(modified_row):
                if j > modified_row.index(number):
                    uniqueness = False
                    break

    return uniqueness


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    False
    """
    horizontal_visibility = True
    for row in board:
        if board.index(row) != 0 and board.index(row) != len(board)-1:
            hint_right = row[0]
            hint_left = row[-1]
            row_visibility_right = True
            row_visibility_left = True
            if hint_right != '*':
                row_visibility_right = left_to_right_check(row,int(hint_right))
            if hint_left != '*':
                reversed_row = row[::-1]
                row_visibility_left = left_to_right_check(reversed_row,int(hint_left))
            if not row_visibility_left or not row_visibility_right:
                horizontal_visibility = False
                break
    return horizontal_visibility



def empty_columns(board):
    """Returns list of "" with length equal to length of expected column.
    >>> empty_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
 '*41532*', '*2*1***'])
    ['', '', '', '', '', '', '']
    """
    columns = []
    while len(columns)!= len(board[0]):
        columns.append("")
    return columns


def fill_columns(columns,board):
    """Returns list of columns of the board.
    >>> fill_columns(['', '', '', '', '', '', ''],['***21**', '412453*', '423145*',\
 '*543215', '*35214*', '*41532*', '*2*1***'])
    ['*44****', '*125342', '*23451*', '2413251', '154213*', '*35142*', '***5***']
    """
    for i in range(len(columns)):
        for row in board:
            columns[i]+=row[i]
    return columns


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    columns_empt = empty_columns(board)
    columns = fill_columns(columns_empt,board)
    uniqueness = check_uniqueness_in_rows(columns)
    visibility = check_horizontal_visibility(columns)
    return uniqueness and visibility


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    finished = check_not_finished_board(board)
    rows = check_uniqueness_in_rows(board) and check_horizontal_visibility(board)
    columns = check_columns(board)
    return finished and rows and columns

if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
