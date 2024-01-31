
import pygame
from board import CheckersBoard

def main():
    pygame.init()

    # Set up the game window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Checkers Game")

    clock = pygame.time.Clock()
    running = True

    # Create an instance of the CheckersBoard
    checkers_board = CheckersBoard()

    current_player = 'o'  # Initial player (can be 'x' or 'o')
    selected_piece = None  # To store the selected piece position

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle user input for making moves
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // checkers_board.square_size
                clicked_col = mouse_pos[0] // checkers_board.square_size

                if selected_piece is None:
                    # If no piece is selected, check if the clicked position contains a piece of the current player
                    if checkers_board.board[clicked_row][clicked_col].lower() == current_player:
                        selected_piece = (clicked_row, clicked_col)
                elif checkers_board.is_valid_move(current_player, selected_piece[0], selected_piece[1], clicked_row, clicked_col):
                    # If a piece is selected, try to move to the clicked position
                    checkers_board.move_piece(selected_piece, (clicked_row, clicked_col))
                    selected_piece = None  # Reset selected piece after a valid move

                    # Switch turns only after a valid move
                    current_player = 'o' if current_player == 'x' else 'x'

        # Update game logic here
    
        # Display the board
        checkers_board.display()

        # Highlight possible moves for the selected piece (for demonstration purposes)
        if selected_piece is not None:
            row, col = selected_piece
            possible_moves = checkers_board.get_possible_moves(current_player, row, col)
            for move in possible_moves:
                pygame.draw.rect(checkers_board.screen, (0, 255, 0, 100),
                                 (move[1] * checkers_board.square_size, move[0] * checkers_board.square_size,
                                  checkers_board.square_size, checkers_board.square_size))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
