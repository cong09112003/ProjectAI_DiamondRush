import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Function start game
def start_game():
    pass    

# Function undo
def undo():
    pass

root = tk.Tk()
root.title("Game Interface - 2 Players")

style = ThemedStyle(root)
style.set_theme("plastik")

# Phần giao diện cho bên trái
player1_frame = ttk.LabelFrame(root, text="Player 1", padding=(10, 10))
player1_frame.grid(row=0, column=0, padx=10, pady=10)

# Combobox chọn agent
player1_options = ttk.Combobox(player1_frame, values=["AI", "Human"])
player1_options.set("AI")
player1_options.grid(row=0, column=0, padx=10, pady=10)

# Combobox chọn thuật toán
algorithm_options1 = ttk.Combobox(player1_frame, values=["Algorithm 1", "Algorithm 2"])
algorithm_options1.set("Algorithm 1")
algorithm_options1.grid(row=1, column=0, padx=10, pady=10)

# Button để chạy thuật toán
start_button1 = ttk.Button(player1_frame, text="Start", command=start_game)
start_button1.grid(row=2, column=0, padx=10, pady=10)

# Button để quay lại bước trước đó
undo_button1 = ttk.Button(player1_frame, text="Undo", command=undo)
undo_button1.grid(row=3, column=0, padx=10, pady=10)

# Canvas để chứa màn hình game
game_canvas1 = tk.Canvas(player1_frame, width=300, height=150, bg="white")
game_canvas1.grid(row=4, column=0, padx=10, pady=10)

# Thời gian chạy thuật toán
time_label1 = ttk.Label(player1_frame, text="Time: 0")
time_label1.grid(row=5, column=0, padx=10, pady=10)

#Số bước chạy thuật toán
step_label1 = ttk.Label(player1_frame, text="Step: 0")
step_label1.grid(row=5, column=1, padx=10, pady=10)

# Phần giao diện cho bên phải, tất cả đều tương tự ở trên
player2_frame = ttk.LabelFrame(root, text="Player 2", padding=(10, 10))
player2_frame.grid(row=0, column=1, padx=10, pady=10)

player2_options = ttk.Combobox(player2_frame, values=["AI", "Human"])
player2_options.set("AI")
player2_options.grid(row=0, column=0, padx=10, pady=10)

algorithm_options2 = ttk.Combobox(player2_frame, values=["Algorithm 1", "Algorithm 2"])
algorithm_options2.set("Algorithm 1")
algorithm_options2.grid(row=1, column=0, padx=10, pady=10)

start_button2 = ttk.Button(player2_frame, text="Start", command=start_game)
start_button2.grid(row=2, column=0, padx=10, pady=10)


undo_button2 = ttk.Button(player2_frame, text="Undo", command=undo)
undo_button2.grid(row=3, column=0, padx=10, pady=10)

game_canvas2 = tk.Canvas(player2_frame, width=300, height=150, bg="white")
game_canvas2.grid(row=4, column=0, padx=10, pady=10)

time_label2 = ttk.Label(player2_frame, text="Time: 0")
time_label2.grid(row=5, column=0, padx=10, pady=10)

step_label2 = ttk.Label(player2_frame, text="Step: 0")
step_label2.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()