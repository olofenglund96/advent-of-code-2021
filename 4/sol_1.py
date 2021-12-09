import sys
sys.path.extend(['..', '.'])
import decorators
import numpy as np
from pprint import pprint

def board_from_lines(lines):
  board = np.ndarray((5,5))
  for i,l in enumerate(lines):
    bl = l.split(' ')
    board[i,:] = [int(n) for n in filter(lambda n: n != '', bl)]

  return board


def parse_boards(lines):
  boards = []
  for i in range(0, len(lines), 6):
    curr_board = board_from_lines(lines[i:i+5])
    boards.append(curr_board)

  return boards


def has_complete_axis(state_board):
  for row in state_board:
    if sum(row) == 5:
      return True

  for col in state_board.T:
    if sum(col) == 5:
      return True

  return False

def sum_noncomplete(state_board, board):
  ixs = np.where(state_board == 0)
  return np.sum(board[ixs])


@decorators.with_input
def main(lines):
  seq = [int(l) for l in lines[0].split(',')]
  boards = parse_boards(lines[2:])
  state_boards = [np.zeros((5,5)) for i in range(len(boards))]


  for s in seq:
    finished_boards = []
    for i, board in enumerate(boards):
      match = np.where(board == s)
      print(i, match)
      state_boards[i][match] = 1

      # print(f"{s=}")
      # pprint(board)
      # pprint(state_boards[i])
      # input()

      if has_complete_axis(state_boards[i]):
        finished_boards.append(i)

    finished_boards = sorted(finished_boards, reverse=True)
    for ix in finished_boards:
      if len(boards) == 1:
        board = boards[ix]
        state_board = state_boards[ix]
        print(s * sum_noncomplete(state_board, board))
        return
      del boards[ix]
      del state_boards[ix]


if __name__ == "__main__":
  main()
