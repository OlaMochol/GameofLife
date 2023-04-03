from board import init, display
from config import Settings

settings=Settings()

board = init(settings.width, settings.height)

board[4][5] = 1
board[4][6] = 1
board[5][5] = 1

display(board)