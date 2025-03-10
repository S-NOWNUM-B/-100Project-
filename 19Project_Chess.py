class Chess:
    def __init__(self, color: str, position: tuple):
        self.color = color
        self.position = position

    def possible_moves(self, board):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассах")

    def move(self, new_position, board):
        if new_position in self.possible_moves(board):
            self.position = new_position
        else:
            raise ValueError(f"Недопустимый ход для {self.__class__.__name__}")

class Pawn(Chess):
    def possible_moves(self, board):
        moves = []
        x, y = self.position
        direction = 1 if self.color == "white" else -1
        if board.is_empty((x, y + direction)):
            moves.append((x, y + direction))
        for dx in [-1, 1]:
            attack_pos = (x + dx, y + direction)
            if board.is_enemy(self.color, attack_pos):
                moves.append(attack_pos)
        return moves

class Rook(Chess):
    def possible_moves(self, board):
        moves = []
        x, y = self.position
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            while board.is_empty((nx, ny)):
                nx = nx + dx
                ny = ny + dy
            if board.is_enemy(self.color, (nx, ny)):
                moves.append((nx, ny))
        return moves

class ChessBoard:
    def __init__(self):
        self.board = {}
        self.setup_pieces()

    def setup_pieces(self):
        for x in range(8):
            self.board[(x, 1)] = Pawn('white', (x, 1))
            self.board[(x, 6)] = Pawn('black', (x, 6))

        self.board[(0, 0)] = Rook('white', (0, 0))
        self.board[(7, 0)] = Rook('white', (7, 0))
        self.board[(0, 7)] = Rook('black', (0, 7))
        self.board[(7, 7)] = Rook('black', (7, 7))

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8

    def is_empty(self, position):
        return position not in self.board

    def is_enemy(self, color, position):
        return position in self.board and self.board[position].color != color

    def move_piece(self, from_pos, to_pos):
        if from_pos not in self.board:
            raise ValueError("На начальной позиции нет фигуры!")

        piece = self.board[from_pos]
        if to_pos in piece.possible_moves(self):
            self.board[to_pos] = piece
            del self.board[from_pos]
            piece.position = to_pos
        else:
            raise ValueError("Недопустимый ход!")

    def display(self):
        for y in range(7, -1, -1):
            row = ""
            for x in range(8):
                piece = self.board.get((x, y), None)
                if piece:
                    row += f" {piece.__class__.__name__[0]} "
                else:
                    row += " . "
            print(row)
        print("\n")

board = ChessBoard()
board.display()

print("Ходы пешки на (1, 1):", board.board[(1, 1)].possible_moves(board))
board.move_piece((1, 1), (1, 2))
board.display()