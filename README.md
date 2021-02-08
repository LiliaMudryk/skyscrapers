There is only one module in this project scyscrapers.py.

This module will allow you to check whether there is a winning combination
on the board in skyscrapers game.

The module consists of functions:
  1) def read_input(path: str)- Read game board file from path. Return list of str.

  2) def left_to_right_check(input_line: str, pivot: int) - Check row-wise visibility from left to right.
     Return True if number of building from the left-most hint is visible looking to the right, False otherwise.

  3) def check_not_finished_board(board: list) - Check if skyscraper board is not finished, i.e., '?' present on the game board.
     Return True if finished, False otherwise.

  4) def check_uniqueness_in_rows(board: list) - Check buildings of unique height in each row.
     Return True if buildings in a row have unique length, False otherwise.

  5) def check_horizontal_visibility(board: list) - Check row-wise visibility (left-right and vice versa)
     Return True if all horizontal hints are satisfiable, False otherwise.

  6) def empty_columns(board) - Returns list of "" with length equal to length of expected column

  7) def fill_columns(columns,board) - Returns list of columns of the board.

  8) def check_columns(board: list) - Check column-wise compliance of the board for uniqueness (buildings of unique height)
     and visibility (top-bottom and vice versa).

  9) def check_skyscrapers(input_path: str) - Main function to check the status of skyscraper game board.
     Return True if the board status is compliant with the rules, False otherwise.

