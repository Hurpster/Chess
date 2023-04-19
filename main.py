# two player chess in python


import pygame

# getting access for pygame stuff
pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Two Player Chess")
# font_size = 20
font = pygame.font.Font('TMR.ttf', 20)
big_font = pygame.font.Font("TMR.ttf", 40)
medium_font = pygame.font.Font("TMR.ttf", 30)

timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

turn = 0
selection = 100
valid_moves = []

# loading images(king, queen, rook, bishop, knight, pawn) white&black
# king white
white_king = pygame.image.load('pieces_images/White_King.png')
white_king = pygame.transform.scale(white_king, (100, 100))  # piece_image_size
white_king_discarded = pygame.transform.scale(white_king, (45, 45))
# queen white
white_queen = pygame.image.load('pieces_images/White_Queen.png')
white_queen = pygame.transform.scale(white_queen, (100, 100))  # piece_image_size
white_queen_discarded = pygame.transform.scale(white_queen, (45, 45))
# rook white
white_rook = pygame.image.load('pieces_images/White_Rook.png')
white_rook = pygame.transform.scale(white_rook, (100, 100))
white_rook_discarded = pygame.transform.scale(white_rook, (45, 45))
# bishop white
white_bishop = pygame.image.load('pieces_images/White_Bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (100, 100))
white_bishop_discarded = pygame.transform.scale(white_bishop, (45, 45))
# knight white
white_knight = pygame.image.load('pieces_images/White_Knight.png')
white_knight = pygame.transform.scale(white_knight, (100, 100))
white_knight_discarded = pygame.transform.scale(white_knight, (45, 45))
# pawn white
white_pawn = pygame.image.load('pieces_images/White_Pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (100, 100))
white_pawn_discarded = pygame.transform.scale(white_pawn, (35, 35))

# king black
black_king = pygame.image.load('pieces_images/Black_King.png')
black_king = pygame.transform.scale(black_king, (100, 100))  # piece_image_size
black_king_discarded = pygame.transform.scale(black_king, (45, 45))
# queen black
black_queen = pygame.image.load('pieces_images/Black_Queen.png')
black_queen = pygame.transform.scale(black_queen, (100, 100))  # piece_image_size
black_queen_discarded = pygame.transform.scale(black_queen, (45, 45))
# rook black
black_rook = pygame.image.load('pieces_images/Black_Rook.png')
black_rook = pygame.transform.scale(black_rook, (100, 100))
black_rook_discarded = pygame.transform.scale(black_rook, (45, 45))
# bishop black
black_bishop = pygame.image.load('pieces_images/Black_Bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (100, 100))
black_bishop_discarded = pygame.transform.scale(black_bishop, (45, 45))
# knight black
black_knight = pygame.image.load('pieces_images/Black_Knight.png')
black_knight = pygame.transform.scale(black_knight, (100, 100))
black_knight_discarded = pygame.transform.scale(black_knight, (45, 45))
# pawn black
black_pawn = pygame.image.load('pieces_images/Black_Pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (100, 100))
black_pawn_discarded = pygame.transform.scale(black_pawn, (35, 35))

white_images = [white_king, white_queen, white_rook, white_bishop, white_knight, white_pawn]
white_images_discarded = [white_king_discarded, white_queen_discarded, white_rook_discarded,
                          white_bishop_discarded, white_knight_discarded, white_pawn_discarded]

black_images = [black_king, black_queen, black_rook, black_bishop, black_knight, black_pawn]
black_images_discarded = [black_king_discarded, black_queen_discarded, black_rook_discarded,
                          black_bishop_discarded, black_knight_discarded, black_pawn_discarded]

pieces_list = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

counter = 0
winner = ''
game_over = ''


# check variables


# draw board
def chess_board():
    for i in range(64):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'gray31', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'gray31', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray65', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'orange4', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'orange4', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to move!', 'White: Play a move!',
                       'Black: Select a Piece to move!', 'Black: Play a move!']
        screen.blit(big_font.render(status_text[turn], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 835))


def chess_pieces():
    for i in range(len(white_pieces)):
        index = pieces_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0] * 100 + 2, white_location[i][1] * 100 + 2))
        else:
            screen.blit(white_images[index], (white_location[i][0] * 100 + 2, white_location[i][1] * 100 + 2))

    for i in range(len(black_pieces)):
        index = pieces_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0] * 100 + 2, black_location[i][1] * 100 + 2))
        else:
            screen.blit(black_images[index], (black_location[i][0] * 100 + 2, black_location[i][1] * 100 + 2))


# check all pieces valid options
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check valid pawn moves
def check_pawn(position, color, en_passant=None):
     moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list



# check valid rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location
    for i in range(4):  # down, up,  right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':

        friends_list = white_location
    else:

        friends_list = black_location

    # max knight options are 8, check the spots
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7:
            moves_list.append(target)

    return moves_list


# check valid bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False

    return moves_list


# check valid queen moves, combine rook & bishop
def check_queen(position, color):
    moves_list = check_rook(position, color)
    move_list = check_bishop(position, color)
    for i in range(len(move_list)):
        moves_list.append(move_list[i])
    return moves_list


# check valid king moves
def check_king(position, color):
    moves_list = []
    if color == 'white':

        friends_list = white_location
    else:

        friends_list = black_location

    # 8 squares, any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    if turn < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured
def draw_captured():
    order = ["king", "queen", "rook", "bishop", "knight", "pawn"]

    # Sort captured white pieces
    captured_pieces_white_sorted = sorted(captured_pieces_white, key=lambda piece: order.index(piece))

    # Draw sorted white pieces
    for i, captured_piece in enumerate(captured_pieces_white_sorted):
        index = pieces_list.index(captured_piece)
        screen.blit(black_images_discarded[index], (825, 5 + 50 * i))

    # Sort captured black pieces
    captured_pieces_black_sorted = sorted(captured_pieces_black, key=lambda piece: order.index(piece))

    # Draw sorted black pieces
    for i, captured_piece in enumerate(captured_pieces_black_sorted):
        index = pieces_list.index(captured_piece)
        screen.blit(white_images_discarded[index], (925, 5 + 50 * i))


def draw_check():
    if turn < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_location[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_location[king_index][0] * 100 + 1,
                                                              white_location[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_location[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_location[king_index][0] * 100 + 1,
                                                               black_location[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press Enter to Restart!', True, 'white'), (210, 240))


# main game loop
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')

run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('azure4')
    chess_board()
    chess_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            if turn <= 1:
                if click_coord == (8, 8) or click_coord == (9, 8):
                    winner = 'black'
                if click_coord in white_location:
                    selection = white_location.index(click_coord)
                    if turn == 0:
                        turn = 1
                if click_coord in valid_moves and selection != 100:
                    white_location[selection] = click_coord
                    if click_coord in black_location:
                        black_piece = black_location.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn = 2
                    selection = 100
                    valid_moves = []
            if turn > 1:
                if click_coord == (8, 8) or click_coord == (9, 8):
                    winner = 'white'
                if click_coord in black_location:
                    selection = black_location.index(click_coord)
                    if turn == 2:
                        turn = 3
                if click_coord in valid_moves and selection != 100:
                    black_location[selection] = click_coord
                    if click_coord in white_location:
                        white_piece = white_location.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                white_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

                black_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_location, 'black')
                white_options = check_options(white_pieces, white_location, 'white')
    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()
