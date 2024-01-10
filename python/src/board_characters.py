from common import time_execution

'''Given a 'board' of characters and a string 'word' create a boolean function 
    that checks if we can find the word in the board, same cell can only be used once,
    and you can only use rows/columns, diagonal movement is not allowed
'''


@time_execution()
def can_create_iter(board: list[list[str]], word: str) -> bool:
    board: dict[complex, str] = {complex(i, j): c for i, row in enumerate(board)
                                 for j, c in enumerate(row)}
    stack = [(p, 1, set([p])) for p, c in board.items() if c == word[0]]
    while stack:
        pos, char_idx, seen = stack.pop()
        seen = seen.copy()
        for new_pos in [pos+1, pos-1, pos-1j, pos+1j]:
            if new_pos in board and new_pos not in seen:  # Inside bounds and haven't seen before
                seen.add(new_pos)
                if char_idx == len(word):  # Found a full match
                    return True
                if board[new_pos] == word[char_idx]:
                    stack.append((new_pos, char_idx+1, seen))

    return False  # No match found after checking all cells


@time_execution()
def can_create_iter_v2(board: list[list[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    stack = [((i, j), 1, [[False]*cols for _ in range(rows)]) for i in range(rows)
             for j in range(cols) if board[i][j] == word[0]]

    while stack:
        (x, y), char_idx, seen = stack.pop()
        if seen[x][y]:
            continue

        seen = seen.copy()
        seen[x][y] = True

        if char_idx == len(word):  # found a full match
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == word[char_idx]:
                stack.append(((nx, ny), char_idx + 1, seen))

    return False  # No match found after checking all cells


@time_execution()
def can_create_rec(board: list[list[str]], word: str) -> bool:
    def search_word(x: int, y: int, char_idx: int, seen: list[list[bool]]) -> bool:
        if char_idx == len(word):  # Means we've found the full word
            return True
        # Only proceed if it's inside bounds, haven't seen before and the character at that position corresponds
        if 0 <= x < row and 0 <= y < col and not (x, y) in seen and word[char_idx] == board[x][y]:
            seen.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if search_word(x+dx, y+dy, char_idx+1, seen):
                    return True
            else:  # When backtracking change all the positions back to False
                seen.remove((x, y))
                return False

        return False

    row = len(board)
    col = len(board[0])
    seen = set([])

    # For every first character of a wanted word, check recursively whether we can make the rest of the word
    return any(search_word(i, j, 0, seen) for i in range(row)
               for j in range(col) if board[i][j] == word[0])


@time_execution()
def can_create_rec_v2(board: list[list[str]], word: str) -> bool:
    def search_word(x: int, y: int, char_idx: int, seen: list[list[bool]]) -> bool:
        if char_idx == len(word):  # Means we've found the full word
            return True
        # Only proceed if it's inside bounds, haven't seen before and the character at that position corresponds
        if 0 <= x < row and 0 <= y < col and not seen[x][y] and word[char_idx] == board[x][y]:
            seen[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if search_word(x+dx, y+dy, char_idx+1, seen):
                    return True
            else:  # When backtracking change all the positions back to False
                seen[x][y] = False
                return False

        return False

    row = len(board)
    col = len(board[0])
    seen = [[False]*col for _ in range(row)]

    # For every first character of a wanted word, check recursively whether we can make the rest of the word
    return any(search_word(i, j, 0, seen) for i in range(row)
               for j in range(col) if board[i][j] == word[0])


board = [['K', 'I', 'N', 'T'],
         ['B', 'I', 'N', 'S'],
         ['G', 'N', 'Y', 'I'],
         ['U', 'O', 'E', 'D'],
         ['D', 'I', 'B', 'V'],
         ['H', 'I', 'R', 'T']]

print(can_create_iter(board, "INSIDE"))
print(can_create_iter(board, "INNNN"))
print(can_create_iter_v2(board, "INSIDE"))
print(can_create_iter_v2(board, "INNNN"))
print(can_create_rec(board, "INSIDE"))
print(can_create_rec(board, "INNNN"))
print(can_create_rec_v2(board, "INSIDE"))
print(can_create_rec_v2(board, "INNNN"))
