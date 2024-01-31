
import pygame

class CheckersBoard:
    def __init__(self):
        # Initialize the board here 
        self.board = [
            ['_', 'o', '_', 'o', '_', 'o', '_', 'o'],
            ['o', '_', 'o', '_', 'o', '_', 'o', '_'],
            ['_', 'o', '_', 'o', '_', 'o', '_', 'o'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['x', '_', 'x', '_', 'x', '_', 'x', '_'],
            ['_', 'x', '_', 'x', '_', 'x', '_', 'x'],
            ['x', '_', 'x', '_', 'x', '_', 'x', '_']
        ]

        # Set up pygame display
        self.square_size = 75
        self.screen = pygame.display.set_mode((self.square_size * 8, self.square_size * 8))
        self.current_player = 'x'  # Initialize the current player
    
    
    
    def get_possible_moves(self, current_player, row, col):
        possible_moves = []

        # Check right move
        right_move = (row + 1, col + 1) if current_player == 'x' else (row - 1, col + 1)
        if self.is_valid_move(current_player, row, col, *right_move):
            possible_moves.append(right_move)

        # Check left move
        left_move = (row + 1, col - 1) if current_player == 'x' else (row - 1, col - 1)
        if self.is_valid_move(current_player, row, col, *left_move):
            possible_moves.append(left_move)

        # If the piece is a king, check moves in both directions
        if self.board[row][col].isupper():  # Check if the piece is a king
            right_move = (row + 1, col - 1) if current_player == 'x' else (row - 1, col - 1)
            left_move = (row + 1, col + 1) if current_player == 'x' else (row - 1, col + 1)

            if self.is_valid_move(current_player, row, col, *right_move):
                possible_moves.append(right_move)

            if self.is_valid_move(current_player, row, col, *left_move):
                possible_moves.append(left_move)

        return possible_moves
    
