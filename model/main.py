
DEFULT_DIMENSION = 8

class Board:
	def __init__(self):
		self.dimension = DEFULT_DIMENSION
		initial_placement()

	def __init__(self, d):
		self.dimension = d if d > 2 and d % 2 != 0 else DEFULT_DIMENSION
		initial_placement()

	def initial_placement(self):
		self.board = [[0]*self.dimension] * self.dimension
		self.board[self.dimension // 2 - 1][self.dimension // 2 - 1] = 1
		self.board[self.dimension // 2 - 1][self.dimension // 2] = -1
		self.board[self.dimension // 2][self.dimension // 2 - 1] = -1
		self.board[self.dimension // 2][self.dimension // 2] = 1
		self.current_player = -1

	def change_player(self):
		self.current_player = -self.current_player 
