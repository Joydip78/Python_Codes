import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

SERVER_IP = input("Enter Server IP Address: ")
PORT = 5555

BOARD_SIZE = 5
NUM_SHIPS = 3

class BattleshipClient:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Battleship - Client")
        self.status = tk.Label(self.window, text="Connecting to server...")
        self.status.pack()

        self.my_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.enemy_board = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.ships_placed = 0
        self.turn = False

        self.create_boards()
        self.connect_to_server()

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
            self.conn.sendall("READY".encode())
            self.status.config(text="Ships placed. Waiting for your turn...")

    def connect_to_server(self):
        threading.Thread(target=self.connection_thread, daemon=True).start()

    def connection_thread(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((SERVER_IP, PORT))
        self.status.config(text="Connected to server. Place your ships.")
        threading.Thread(target=self.receive_loop, daemon=True).start()

    def receive_loop(self):
        while True:
            data = self.conn.recv(1024).decode()
            if data.startswith("FIRE"):
                i, j = map(int, data.split()[1:])
                hit = self.my_board[i][j] == "S"
                self.my_board[i][j] = "X" if hit else "O"
                self.buttons[i][j].config(bg="red" if hit else "blue", text="X" if hit else "O")
                self.conn.sendall(f"HIT {int(hit)}".encode())
                self.turn = True
                self.status.config(text="Your turn!" if not hit else "They hit you!")
            elif data.startswith("HIT"):
                hit = data.split()[1] == "1"
                self.status.config(text="🎯 Hit!" if hit else "💨 Miss!")

    def fire(self, i, j):
        if not self.turn or self.enemy_board[i][j] != "~":
            return
        self.conn.sendall(f"FIRE {i} {j}".encode())
        self.enemy_board[i][j] = "O"
        self.turn = False
        self.status.config(text="Waiting for opponent...")

# Run Client
if __name__ == "__main__":
    BattleshipClient()
