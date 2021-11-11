import pygame
import numpy as np
import cmath
import time
import math
import json
import atexit


def get_around(pos, arr):
    surroundings = []
    n = complex(1, 0)
    for i in range(2):
        for j in range(4):
            x = int(pos[0] + n.real)
            y = int(pos[1] + n.imag)
            if 0 > x:
                x = len(arr[0])-1
            elif len(arr[0])-1 < x:
                x = 0
            if 0 > y:
                y = len(arr)-1
            elif len(arr)-1 < y:
                y = 0
            surroundings.append(arr[y][x])
            n *= cmath.sqrt(-1)
        n = complex(1, 1)
    total = sum(surroundings)
    return total


def save(data, file):
    with open(file, "w") as fil:
        json.dump(data, fil)


def change(pos, arr):
    sum_ = get_around(pos, arr)
    cell_val = arr[pos[1]][pos[0]]
    new_val = 0
    if cell_val == 0:
        if sum_ == 3:
            new_val = 1
    elif cell_val == 1:
        if sum_ < 2:
            new_val = 0
        elif 2 == sum_ or sum_ == 3:
            new_val = 1
        elif sum_ > 3:
            new_val = 0
    return new_val


def get_data(board):
    new_board = np.zeros((len(board), len(board[0])))
    for y in range(len(board)):
        for x in range(len(board[y])):
            new_board[y][x] = change((x, y), board)
    board = new_board
    return board


def main():
    file = "boards.json"
    f = open(file,)
    window_height = 500
    window_width = 500
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    img = pygame.image.load("Icon.png")
    pygame.display.set_icon(img)
    board_height = 50
    board_width = 50
    board_size = (board_height, board_width)
    board = np.zeros(board_size)
    pause = False
    mouse_down = False
    mouse_two_down = False
    data = json.load(f)
    atexit.register(save, data, file)
    while True:
        screen.fill((0, 0, 0))
        block_size_x = (window_width-len(board[0])) / len(board[0])
        block_size_y = (window_height-len(board)) / len(board)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(file, "w") as fil:
                    json.dump(data, fil)
                f.close()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_p:
                    if not pause:
                        pause = True
                    else:
                        pause = False
                elif event.key == pygame.K_s:
                    pause = False
                if event.key == pygame.K_r:
                    board = np.zeros(board_size)
                if keys[pygame.K_w]:
                    if keys[pygame.K_1]:
                        board = np.array(data["1"])
                    if keys[pygame.K_2]:
                        board = np.array(data["2"])
                    if keys[pygame.K_3]:
                        board = np.array(data["3"])
                    if keys[pygame.K_4]:
                        board = np.array(data["4"])
                    if keys[pygame.K_5]:
                        board = np.array(data["5"])
                    if keys[pygame.K_6]:
                        board = np.array(data["6"])
                    if keys[pygame.K_7]:
                        board = np.array(data["7"])
                    if keys[pygame.K_8]:
                        board = np.array(data["8"])
                    if keys[pygame.K_9]:
                        board = np.array(data["9"])
                    if keys[pygame.K_0]:
                        board = np.array(data["0"])
                if keys[pygame.K_q]:
                    if keys[pygame.K_1]:
                        data["1"] = board.tolist()
                    if keys[pygame.K_2]:
                        data["2"] = board.tolist()
                    if keys[pygame.K_3]:
                        data["3"] = board.tolist()
                    if keys[pygame.K_4]:
                        data["4"] = board.tolist()
                    if keys[pygame.K_5]:
                        data["5"] = board.tolist()
                    if keys[pygame.K_6]:
                        data["6"] = board.tolist()
                    if keys[pygame.K_7]:
                        data["7"] = board.tolist()
                    if keys[pygame.K_8]:
                        data["8"] = board.tolist()
                    if keys[pygame.K_9]:
                        data["9"] = board.tolist()
                    if keys[pygame.K_0]:
                        data["0"] = board.tolist()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                if event.button == 3:
                    mouse_two_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
                if event.button == 3:
                    mouse_two_down = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                window_width = event.w
                window_height = event.h
        if not pause:
            board = get_data(board)
        if mouse_down:
            x, y = int(math.floor(mouse_x/(block_size_x + 1))), int(math.floor(mouse_y/(block_size_y + 1)))
            board[y][x] = 1
        if mouse_two_down:
            x, y = int(math.floor(mouse_x / (block_size_x + 1))), int(math.floor(mouse_y / (block_size_y + 1)))
            board[y][x] = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                rect = pygame.Rect(x * (block_size_x + 1), y * (block_size_y + 1), block_size_x, block_size_y)
                if board[y][x] == 0:
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                elif board[y][x] == 1:
                    pygame.draw.rect(screen, (200, 200, 200), rect)
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
