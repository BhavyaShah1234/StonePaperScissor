import cv2 as cv
from HandTracking import HandDetector
import keyboard as kb
import random as rn

hd = HandDetector(False, 1, 0.75, 0.5)
cap = cv.VideoCapture(0)
choice = False


def get_hand_and_fingers(image):
    h = 'Right'
    f = [1, 1, 1, 1, 1]
    points_arr = hd.get_specific_coordinates(image=image, points=range(21))
    if len(points_arr) != 0:
        if points_arr[4][1] > points_arr[17][1]:
            h = 'Right'
            if points_arr[4][1] < points_arr[2][1]:
                f[0] = 0
            if points_arr[8][2] > points_arr[6][2]:
                f[1] = 0
            if points_arr[12][2] > points_arr[10][2]:
                f[2] = 0
            if points_arr[16][2] > points_arr[14][2]:
                f[3] = 0
            if points_arr[20][2] > points_arr[18][2]:
                f[4] = 0
        else:
            h = 'Left'
            if points_arr[4][1] > points_arr[2][1]:
                f[0] = 0
            if points_arr[8][2] > points_arr[6][2]:
                f[1] = 0
            if points_arr[12][2] > points_arr[10][2]:
                f[2] = 0
            if points_arr[16][2] > points_arr[14][2]:
                f[3] = 0
            if points_arr[20][2] > points_arr[18][2]:
                f[4] = 0
    return h, f


play_again = False
r_key = 'q'
while not play_again:
    while not choice:
        _, img = cap.read()
        img = hd.draw_all(img)
        img = cv.putText(img, 'SHOW YOUR HAND', (100, 50), cv.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 255), 2)
        img = cv.putText(img, 'CAN YOU SEE THE LINES?', (5, 100), cv.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0), 2)
        img = cv.putText(img, 'YES', (290, 180), cv.FONT_ITALIC, 1.5, (255, 0, 0), 2)
        pts = hd.get_specific_coordinates(img, points=[8])
        if len(pts) != 0:
            x = pts[0][1]
            y = pts[0][2]
            if 280 < x < 380 and 135 < y < 185:
                choice = True
                break
        cv.imshow('Stone Paper Scissor', img)
        cv.waitKey(1)

    winner = False
    user = 0
    comp = 0
    stone = cv.imread('stone.png')
    paper = cv.imread('paper.png')
    scissor = cv.imread('scissor.png')
    move_size = 150
    stone = cv.resize(stone, (move_size, move_size))
    paper = cv.resize(paper, (move_size, move_size))
    scissor = cv.resize(scissor, (move_size, move_size))
    comp_moves = ['stone', 'paper', 'scissor']
    move_dict = {'stone': stone, 'paper': paper, 'scissor': scissor}
    comp_move = 'stone'
    while not winner:
        _, img = cap.read()
        img = cv.putText(img, f'USER:{user}', (200, 50), cv.FONT_HERSHEY_PLAIN, 2.5, (0, 255, 255), 2)
        img = cv.putText(img, f'COMP:{comp}', (450, 50), cv.FONT_HERSHEY_PLAIN, 2.5, (0, 255, 255), 2)
        height, width, channel = img.shape
        img1 = hd.draw_all(img)
        img2 = cv.putText(img, f'PRESS {r_key} WHEN READY', (50, 400), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 2)
        if kb.is_pressed(r_key):
            comp_move = rn.choice(comp_moves)
            user_hand, user_finger = get_hand_and_fingers(img)
            if user_hand == 'Right':
                if user_finger[1] == 1 and user_finger[2] == 1 and user_finger[3] == 0 and user_finger[4] == 0:
                    user_move = 'scissor'
                    print(comp_move, user_move)
                    if comp_move == 'stone':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'paper':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
                    else:
                        pass
                elif user_finger[1] == 1 and user_finger[2] == 1 and user_finger[3] == 1 and user_finger[4] == 1:
                    user_move = 'paper'
                    print(comp_move, user_move)
                    if comp_move == 'scissor':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'stone':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
                elif user_finger[1] == 0 and user_finger[2] == 0 and user_finger[3] == 0 and user_finger[4] == 0:
                    user_move = 'stone'
                    print(comp_move, user_move)
                    if comp_move == 'paper':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'scissor':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
            elif user_hand == 'Left':
                if user_finger[1] == 1 and user_finger[2] == 1 and user_finger[3] == 0 and user_finger[4] == 0:
                    user_move = 'scissor'
                    print(comp_move, user_move)
                    if comp_move == 'stone':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'paper':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
                    else:
                        pass
                elif user_finger[1] == 1 and user_finger[2] == 1 and user_finger[3] == 1 and user_finger[4] == 1:
                    user_move = 'paper'
                    print(comp_move, user_move)
                    if comp_move == 'scissor':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'stone':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
                elif user_finger[1] == 0 and user_finger[2] == 0 and user_finger[3] == 0 and user_finger[4] == 0:
                    user_move = 'stone'
                    print(comp_move, user_move)
                    if comp_move == 'paper':
                        comp = comp + 1
                        if user == 5 or comp == 5:
                            winner = True
                    elif comp_move == 'scissor':
                        user = user + 1
                        if user == 5 or comp == 5:
                            winner = True
        img[0:move_size, 0:move_size] = move_dict[comp_move]
        cv.imshow('Stone Paper Scissor', img)
        cv.waitKey(1)

    while winner:
        _, img = cap.read()
        img = hd.draw_all(img)
        img = cv.putText(img, 'PLAY AGAIN?', (100, 100), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 0), 2)
        img = cv.putText(img, 'YES', (100, 200), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
        img = cv.putText(img, 'NO', (450, 200), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
        if user == 5:
            img = cv.putText(img, 'THE WINNER IS USER', (50, 50), cv.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0), 2)
        else:
            img = cv.putText(img, 'THE WINNER IS COMPUTER', (0, 50), cv.FONT_HERSHEY_TRIPLEX, 1.4, (0, 255, 0), 2)
        pts = hd.get_specific_coordinates(img, [8])
        if len(pts) > 0:
            x, y = pts[0][1], pts[0][2]
            if 85 < x < 200 and 150 < y < 215:
                play_again = False
                break
            elif 435 < x < 520 and 150 < y < 215:
                play_again = True
                break
        cv.imshow('Stone Paper Scissor', img)
        cv.waitKey(1)
