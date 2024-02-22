import copy


def is_block(board, start, direction):
    x, y = start
    if direction == 'u':
        if board[x - 1][y] == 'w':
            return True
        if board[x - 1][y] == 'd':
            return True
        if board[x - 1][y] == 's':
            if x - 2 < 0:
                return True
            elif board[x - 2][y] == 's' or board[x - 2][y] == 'd' or board[x - 2][y] == 'w':
                return True

    if direction == 'd':
        if board[x + 1][y] == 'w':
            return True
        if board[x + 1][y] == 'd':
            return True
        if board[x + 1][y] == 's':
            if x + 2 >= len(board):
                return True
            elif board[x + 2][y] == 's' or board[x + 2][y] == 'd' or board[x + 2][y] == 'w':
                return True

    if direction == 'l':
        if board[x][y - 1] == 'w':
            return True
        if board[x][y - 1] == 'd':
            return True
        if board[x][y - 1] == 's':
            if y - 2 < 0:
                return True
            elif board[x][y - 2] == 's' or board[x][y - 2] == 'd' or board[x][y - 2] == 'w':
                return True

    if direction == 'r':
        if board[x][y + 1] == 'w':
            return True
        if board[x][y + 1] == 'd':
            return True
        if board[x][y + 1] == 's':
            if y + 2 >= len(board[0]):
                return True
            elif board[x][y + 2] == 's' or board[x][y + 2] == 'd' or board[x][y + 2] == 'w':
                return True

    return False


def get_action(board, start):
    action = []
    rows = len(board)
    cols = len(board[0])
    x, y = start

    if 0 <= x - 1 < rows and 0 <= y < cols and not is_block(board, start, 'u'):
        action.append('u')

    if 0 <= x + 1 < rows and 0 <= y < cols and not is_block(board, start, 'd'):
        action.append('d')

    if 0 <= y - 1 < cols and 0 <= x < rows and not is_block(board, start, 'l'):
        action.append('l')

    if 0 <= y + 1 < cols and 0 <= x < rows and not is_block(board, start, 'r'):
        action.append('r')

    return action


def is_goal(board):
    for row in board:
        if 's' in row:
            return False
    return True


def update_board(board, start, move):
    new_board = copy.deepcopy(board)
    x, y = start

    if board[x][y] == 'ab':
        new_board[x][y] = 'b'
    else:
        new_board[x][y] = 'f'

    if move == 'u':
        if new_board[x - 1][y] == 's':
            if new_board[x - 2][y] == 'b':
                new_board[x - 2][y] = 'd'
            else:
                new_board[x - 2][y] = 's'

        if new_board[x - 1][y] == 'b':
            new_board[x - 1][y] = 'ab'
        else:
            new_board[x - 1][y] = 'a'

    if move == 'd':
        if new_board[x + 1][y] == 's':
            if new_board[x + 2][y] == 'b':
                new_board[x + 2][y] = 'd'
            else:
                new_board[x + 2][y] = 's'

        if new_board[x + 1][y] == 'b':
            new_board[x + 1][y] = 'ab'
        else:
            new_board[x + 1][y] = 'a'

    if move == 'l':
        if new_board[x][y - 1] == 's':
            if new_board[x][y - 2] == 'b':
                new_board[x][y - 2] = 'd'
            else:
                new_board[x][y - 2] = 's'

        if new_board[x][y - 1] == 'b':
            new_board[x][y - 1] = 'ab'
        else:
            new_board[x][y - 1] = 'a'

    if move == 'r':
        if new_board[x][y + 1] == 's':
            if new_board[x][y + 2] == 'b':
                new_board[x][y + 2] = 'd'
            else:
                new_board[x][y + 2] = 's'

        if new_board[x][y + 1] == 'b':
            new_board[x][y + 1] = 'ab'
        else:
            new_board[x][y + 1] = 'a'

    return new_board


def find_start(board):
    for i in range(len(board)):
        if 'a' in board[i]:
            return i, board[i].index('a')
        elif 'ab' in board[i]:
            return i, board[i].index('ab')


def bfs_find(board):
    start = find_start(board)
    open_list = [[start, board, ['F']]]
    visited = [board]
    while True:
        if len(open_list) > 0:
            new_path = open_list.pop(0)
        else:
            return None
        x, y = start = new_path[0]
        board = new_path[1]
        actions = get_action(board, start)

        # up
        afterPath = copy.deepcopy(new_path[2])
        new_start = x - 1, y
        if 'u' in actions:
            afterBoard = update_board(board, start, 'u')
            if afterBoard not in visited:
                afterPath.append('u')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # down
        afterPath = copy.deepcopy(new_path[2])
        new_start = x + 1, y
        if 'd' in actions:
            afterBoard = update_board(board, start, 'd')
            if afterBoard not in visited:
                afterPath.append('d')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # left
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y - 1
        if 'l' in actions:
            afterBoard = update_board(board, start, 'l')
            if afterBoard not in visited:
                afterPath.append('l')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # right
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y + 1
        if 'r' in actions:
            afterBoard = update_board(board, start, 'r')
            if afterBoard not in visited:
                afterPath.append('r')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)


def bfs(board):
    path = bfs_find(board)
    return path


def dfs_find(board, maxLenght):
    start = find_start(board)
    open_list = [[start, board, ['F']]]
    visited = [board]

    while True:
        if len(open_list) > 0:
            new_path = open_list.pop()
        else:
            return None
        x, y = start = new_path[0]
        board = new_path[1]
        actions = get_action(board, start)

        # left
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y - 1
        if 'l' in actions:
            afterBoard = update_board(board, start, 'l')
            if afterBoard not in visited:
                afterPath.append('l')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # up
        afterPath = copy.deepcopy(new_path[2])
        new_start = x - 1, y
        if 'u' in actions:
            afterBoard = update_board(board, start, 'u')
            if afterBoard not in visited:
                afterPath.append('u')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # right
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y + 1
        if 'r' in actions:
            afterBoard = update_board(board, start, 'r')
            if afterBoard not in visited:
                afterPath.append('r')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # down
        afterPath = copy.deepcopy(new_path[2])
        new_start = x + 1, y
        if 'd' in actions:
            afterBoard = update_board(board, start, 'd')
            if afterBoard not in visited:
                afterPath.append('d')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append([new_start, afterBoard, afterPath])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        if len(afterPath) > maxLenght:
            return None


def dfs(board):
    if len(board) == 0:
        return None
    for i in range(1, 7):
        path = dfs_find(board, i * 100)
        if path is not None:
            return path
    return None


def h_calculator(board, start):
    stone_positions = []
    box_positions = []
    x, y = start
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 's':
                stone_positions.append((i, j))
            elif board[i][j] == 'b':
                box_positions.append((i, j))

    sb_distance = 0
    for stone_pos in stone_positions:
        for box_pos in box_positions:
            sb_distance += abs(stone_pos[0] - box_pos[0]) + abs(stone_pos[1] - box_pos[1])

    sa_distance = 0
    for stone_pos in stone_positions:
        sa_distance += abs(stone_pos[0] - x) + abs(stone_pos[1] - y)

    return sb_distance + sa_distance


def min_h(arr):
    min = arr[0]
    for element in arr:
        if element[3] < min[3]:
            min = element
    return min


# has problem
def a_star(board):
    return star_find(board)


def star_find(board):
    start = find_start(board)
    open_list = [[start, board, ['F'], h_calculator(board, start)]]
    visited = [board]

    while True:
        if len(open_list) > 0:
            new_path = min_h(open_list)
            open_list.remove(new_path)
        else:
            return None

        x, y = start = new_path[0]
        board = new_path[1]
        actions = get_action(board, start)

        # left
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y - 1
        if 'l' in actions:
            afterBoard = update_board(board, start, 'l')
            if afterBoard not in visited:
                afterPath.append('l')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append(
                    [new_start, afterBoard, afterPath, h_calculator(afterBoard, new_start) + (len(afterPath) - 1)])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # up
        afterPath = copy.deepcopy(new_path[2])
        new_start = x - 1, y
        if 'u' in actions:
            afterBoard = update_board(board, start, 'u')
            if afterBoard not in visited:
                afterPath.append('u')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append(
                    [new_start, afterBoard, afterPath, h_calculator(afterBoard, new_start) + (len(afterPath) - 1)])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # right
        afterPath = copy.deepcopy(new_path[2])
        new_start = x, y + 1
        if 'r' in actions:
            afterBoard = update_board(board, start, 'r')
            if afterBoard not in visited:
                afterPath.append('r')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append(
                    [new_start, afterBoard, afterPath, h_calculator(afterBoard, new_start) + (len(afterPath) - 1)])
                if afterBoard not in visited:
                    visited.append(afterBoard)

        # down
        afterPath = copy.deepcopy(new_path[2])
        new_start = x + 1, y
        if 'd' in actions:
            afterBoard = update_board(board, start, 'd')
            if afterBoard not in visited:
                afterPath.append('d')
                if is_goal(afterBoard):
                    return afterPath[1:]
                open_list.append(
                    [new_start, afterBoard, afterPath, h_calculator(afterBoard, new_start) + (len(afterPath) - 1)])
                if afterBoard not in visited:
                    visited.append(afterBoard)


# if __name__ == '__main__':
#     board = [['a', 'f', 'b'],
#              ['f', 's', 'f'],
#              ['f', 'f', 'f']
#              ]
#
#     print(a_star(board))
