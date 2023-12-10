import socket
import random

def parse_server(data_stream):
    board = data_stream.decode('utf-8')
    board = board.split("\n")
    for s in board:
        s.split(",")
    return board

def get_input(board):
    # Student Needs to Implement Logic
    rand1 = random.randint(0, 15)
    rand2 = random.randint(0,15)
    return rand1, rand2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 4999))

while True:
    # Receive Board from server
    boardState = s.recv(1024)
    # Send Input to Server
    move0, move1 = get_input(parse_server(boardState))
    s.send((" " + str(move0) + " ").encode())
    s.send((" " + str(move1) + " ").encode())

