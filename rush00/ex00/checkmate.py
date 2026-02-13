def checkmate(board_string):
    rows = board_string.strip().split('\n')
    chess_board = [list(row) for row in rows]
    board_size = len(chess_board)


    king_row, king_col = -1, -1
    for r in range(board_size):
        for c in range(board_size):
            if chess_board[r][c] == 'K':
                king_row, king_col = r, c
                break
    
    if king_row == -1:
        return

    def is_inside(r, c):
        return 0 <= r < board_size and 0 <= c < board_size


    straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    diagonal_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for row_step, col_step in straight_moves:
        current_r, current_c = king_row + row_step, king_col + col_step
        while is_inside(current_r, current_c):
            piece = chess_board[current_r][current_c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            elif piece != '.':
                break
            current_r += row_step
            current_c += col_step

    for row_step, col_step in diagonal_moves:
        current_r, current_c = king_row + row_step, king_col + col_step
        while is_inside(current_r, current_c):
            piece = chess_board[current_r][current_c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            elif piece != '.':
                break
            current_r += row_step
            current_c += col_step

    pawn_threats = [(king_row - 1, king_col - 1), (king_row - 1, king_col + 1)]
    for p_row, p_col in pawn_threats:
        if is_inside(p_row, p_col) and chess_board[p_row][p_col] == 'P':
            print("Success")
            return

    print("Fail")