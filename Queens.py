'''
File: Queens.py

Description: Uses backtracking to find solutions to the 8 queens problem
'''

count = 0
class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution

  def recursive_solve (self, col):
    global count

    #If at end and it has been a solution thus far, check if it has the correct number of queens before another call
    #and print if so. Increment with a global variable outside recursion.
    if (col == self.n):
      Qcount = 0
      for i in self.board:
        for place in i:
          if place == "Q":
            Qcount += 1
          else:
            continue

      if Qcount == self.n:
        self.print_board()
        count += 1
        print()
      
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'

          if (self.recursive_solve (col + 1)):
            return True
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()

    
def main():

  board_size = 0
  while board_size > 8 or board_size < 1:
    board_size = eval(input("Enter the size of board: "))

  print()
  # create a regular chess board
  game = Queens (board_size)

  # place the queens on the board
  game.solve()

  print("There are", count, "solutions for a",board_size,"x",board_size,"board.")

if __name__ == '__main__':
  main()