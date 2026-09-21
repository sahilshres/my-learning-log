import random
import os
import time

BOARD_WIDTH = 20
BOARD_HEIGHT = 10

WALL = '#'
SNAKE = 'O'
FOOD = '*'
EMPTY = ' '

RESET = '\033[0m'
GREEN = '\033[92m'
LIGHT_GREEN = '\033[32m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'


def color(text, shade):
    if os.name == 'nt' and not os.environ.get('WT_SESSION') and not os.environ.get('ANSICON'):
        return text
    return f'{shade}{text}{RESET}'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_board(snake, food):
    board = [[EMPTY for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    for index, (x, y) in enumerate(snake):
        board[y][x] = color('O' if index == 0 else 'o', GREEN if index == 0 else LIGHT_GREEN)
    fx, fy = food
    board[fy][fx] = color(FOOD, RED)

    border = color(WALL * (BOARD_WIDTH + 2), CYAN)
    print(border)
    for row in board:
        print(color(WALL, CYAN) + ''.join(row) + color(WALL, CYAN))
    print(border)


def get_next_position(direction, head):
    x, y = head
    if direction == 'w':
        return x, y - 1
    if direction == 's':
        return x, y + 1
    if direction == 'a':
        return x - 1, y
    if direction == 'd':
        return x + 1, y
    return x, y


def place_food(snake):
    while True:
        food = (random.randrange(1, BOARD_WIDTH - 1), random.randrange(1, BOARD_HEIGHT - 1))
        if food not in snake:
            return food


def game_over(snake):
    head = snake[0]
    if head[0] <= 0 or head[0] >= BOARD_WIDTH - 1:
        return True
    if head[1] <= 0 or head[1] >= BOARD_HEIGHT - 1:
        return True
    return head in snake[1:]


def main():
    snake = [(BOARD_WIDTH // 2, BOARD_HEIGHT // 2)]
    direction = 'd'
    food = place_food(snake)
    score = 0

    try:
        while True:
            clear_screen()
            print(color('================ S N A K E ================', YELLOW))
            print(color(f'  Score: {score}   Length: {len(snake)}', YELLOW))
            draw_board(snake, food)
            print(f'{color("O", GREEN)} snake  {color("*", RED)} food')
            print(color('Move: w = up, s = down, a = left, d = right, q = quit', CYAN))
            move = input('Your move: ').strip().lower()
            if move == 'q':
                break
            if move in ('w', 'a', 's', 'd'):
                direction = move

            next_head = get_next_position(direction, snake[0])
            snake.insert(0, next_head)

            if next_head == food:
                score += 1
                food = place_food(snake)
            else:
                snake.pop()

            if game_over(snake):
                clear_screen()
                print(color('       G A M E   O V E R', RED))
                print(color(f'       Final score: {score}', YELLOW))
                break

            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\nGoodbye!')


if __name__ == '__main__':
    main()
