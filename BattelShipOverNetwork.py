import socket
import threading
import tkinter as tk
from tkinter import messagebox

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5555

BOARD_SIZE = 5
NUM_SHIPS = 3

class BattleshipServer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Battleship - Server")
        self.status = tk.Label(self.window, text="Waiting for client to connect...")
        self.status.pack()

        self.my_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.enemy_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.ships_placed = 0
        self.turn = False
        self.client_conn = None

        self.create_boards()
        self.start_server()

        self.window.mainloop()

    def create_boards(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.buttons = []

        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                btn = tk.Button(self.frame, text="~", width=4, height=2,
                                command=lambda x=i, y=j: self.place_ship(x, y))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def place_ship(self, i, j):
        if self.ships_placed >= NUM_SHIPS:
            return
        if self.my_board[i][j] == "S":
            return
        self.my_board[i][j] = "S"
        self.buttons[i][j].config(bg="gray", text="S")
        self.ships_placed += 1
        if self.ships_placed == NUM_SHIPS:
            self.status.config(text="Waiting for opponent to place ships...")

    def start_server(self):
        threading.Thread(target=self.server_thread, daemon=True).start()

    def server_thread(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        self.client_conn = conn
        self.status.config(text="Client connected! Waiting for ships...")

        threading.Thread(target=self.receive_loop, daemon=True).start()

    def receive_loop(self):
        while True:
            data = self.client_conn.recv(1024).decode()
            if data.startswith("READY"):
                self.turn = True
                self.status.config(text="Opponent ready. Your turn!")
            elif data.startswith("FIRE"):
                i, j = map(int, data.split()[1:])
                hit = self.my_board[i][j] == "S"
                self.my_board[i][j] = "X" if hit else "O"
                self.buttons[i][j].config(bg="red" if hit else "blue", text="X" if hit else "O")
                self.client_conn.sendall(f"HIT {int(hit)}".encode())
                self.turn = True
                self.status.config(text="Your turn!" if not hit else "They hit you!")

    def fire(self, i, j):
        if not self.turn or self.enemy_board[i][j] != "~":
            return
        self.client_conn.sendall(f"FIRE {i} {j}".encode())
        self.enemy_board[i][j] = "O"
        self.turn = False
        self.status.config(text="Waiting for opponent...")

# Run Server
if __name__ == "__main__":
    BattleshipServer()
