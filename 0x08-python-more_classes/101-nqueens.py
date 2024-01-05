def solve_n_queens(n):
    def can_attack(pos1, pos2):
        return (pos1[0] == pos2[0] or pos1[1] == pos2[1] or
                abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]))

    def print_solution(board):
        for row in board:
            print(' '.join(row))
        print()

    def backtrack(n, board, col):
        if col >= n:
            print_solution(board)
            return
        for i in range(n):
            board[col] = '.' * i + 'Q' + '.' * (n - i - 1)
            if all(not can_attack((col, row), (new_col, row)) for new_col, row in enumerate(board) if row[row.index('Q')] == 'Q'):
                backtrack(n, board, col + 1)

    board = ['.' * n for _ in range(n)]
    backtrack(n, board, 0)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_n_queens(n)


if __name__ == "__main__":
    main()
