
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
         def display(self):
        # Display the board using pygame
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                
                if self.board[row][col] != '_':
                    # Draw pieces on the board
                    piece_color = (255, 0, 0) if self.board[row][col] == 'x' else (255, 255, 255)
                    pygame.draw.circle(self.screen, piece_color, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 2 - 5)
        
        pygame.display.flip()

    def move_piece(self, selected_piece, end):
        start_row, start_col = selected_piece
        end_row, end_col = end

        # Check if the move is valid
        if self.is_valid_move(self.current_player, start_row, start_col, end_row, end_col):
            # Perform the move
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = '_'

            # Check for capturing opponent pieces
            if abs(end_row - start_row) == 2:
                captured_row = (start_row + end_row) // 2
                captured_col = (start_col + end_col) // 2
                self.board[captured_row][captured_col] = '_'
        else:
            # Invalid move, handle it accordingly 
            print("Invalid move!")
        
    def is_valid_move(self, current_player, start_row, start_col, end_row, end_col):
        # Check if the end position is within the board bounds
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Check if the end position is empty
        if self.board[end_row][end_col] != '_':
            return False

        # Check if the piece is a king
        is_king = self.board[start_row][start_col].lower() == 'x' and end_row == 0 or self.board[start_row][start_col].lower() == 'o' and end_row == 7

        # Check if the move is diagonal
        if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
            if current_player == 'x' and end_row > start_row and not is_king:
                return False  # Non-king pieces can only move forward for player 'x'
            elif current_player == 'o' and end_row < start_row and not is_king:
                return False  # Non-king pieces can only move forward for player 'o'
            return True  # Valid move for a regular piece

        # Check if the move is a capture (jump over opponent's piece)
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2

            # Check if there is an opponent's piece to capture
            if self.board[captured_row][captured_col].lower() != current_player.lower() and not is_king:
                return True  # Valid capture for a regular piece

            if self.board[captured_row][captured_col].upper() != current_player.upper() and is_king:
                return True  # Valid capture for a king


        return False  # Invalid move
    
    
    
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
    
