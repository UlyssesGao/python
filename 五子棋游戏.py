import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 15
CELL_SIZE = 40
MARGIN = 20
BOARD_PIXEL = BOARD_SIZE * CELL_SIZE
WINDOW_WIDTH = BOARD_PIXEL + MARGIN * 2
WINDOW_HEIGHT = BOARD_PIXEL + MARGIN * 2 + 70

BLACK = "black"
WHITE = "white"


class GomokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = BLACK
        self.game_over = False

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=BOARD_PIXEL + MARGIN * 2, bg="#f0d08a", highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.status_var = tk.StringVar(value="黑方先手")
        label = tk.Label(root, textvariable=self.status_var, font=("微软雅黑", 12), pady=8)
        label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(0, 10))
        tk.Button(btn_frame, text="重新开始", width=12, command=self.restart_game, font=("微软雅黑", 11)).pack()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(BOARD_SIZE):
            x = MARGIN + i * CELL_SIZE
            self.canvas.create_line(x, MARGIN, x, MARGIN + BOARD_PIXEL)
            y = MARGIN + i * CELL_SIZE
            self.canvas.create_line(MARGIN, y, MARGIN + BOARD_PIXEL, y)

        center = BOARD_SIZE // 2
        star_positions = [3, 7, 11]
        for row in star_positions:
            for col in star_positions:
                x = MARGIN + row * CELL_SIZE
                y = MARGIN + col * CELL_SIZE
                self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black")

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is not None:
                    self.draw_stone(row, col, self.board[row][col])

    def draw_stone(self, row, col, color):
        x = MARGIN + col * CELL_SIZE
        y = MARGIN + row * CELL_SIZE
        fill_color = BLACK if color == BLACK else WHITE
        outline = "black" if fill_color == "white" else "white"
        self.canvas.create_oval(x - CELL_SIZE // 2 + 2, y - CELL_SIZE // 2 + 2,
                                x + CELL_SIZE // 2 - 2, y + CELL_SIZE // 2 - 2,
                                fill=fill_color, outline=outline, width=2)

    def handle_click(self, event):
        if self.game_over:
            return

        col = round((event.x - MARGIN) / CELL_SIZE)
        row = round((event.y - MARGIN) / CELL_SIZE)

        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return
        if self.board[row][col] is not None:
            return

        self.board[row][col] = self.current_player
        self.draw_board()

        if self.check_win(row, col, self.current_player):
            self.game_over = True
            winner = "黑方" if self.current_player == BLACK else "白方"
            self.status_var.set(f"{winner}获胜！")
            messagebox.showinfo("游戏结束", f"{winner}赢了！")
            return

        self.current_player = WHITE if self.current_player == BLACK else BLACK
        self.status_var.set(f"{('黑方' if self.current_player == BLACK else '白方')}走棋")

    def check_win(self, row, col, color):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.count_direction(row, col, dr, dc, color)
            count += self.count_direction(row, col, -dr, -dc, color)
            if count >= 5:
                return True
        return False

    def count_direction(self, row, col, dr, dc, color):
        count = 0
        r = row + dr
        c = col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == color:
            count += 1
            r += dr
            c += dc
        return count

    def restart_game(self):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = BLACK
        self.game_over = False
        self.status_var.set("黑方先手")
        self.draw_board()


if __name__ == "__main__":
    root = tk.Tk()
    game = GomokuGame(root)
    root.mainloop()
