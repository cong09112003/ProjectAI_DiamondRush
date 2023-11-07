import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode("System")

app = ct.CTk()
app.geometry("1280x720")
app.title("VS mode")

# Agent 1
#Frame để chứa các element cho agent 1
agent1_frame = ct.CTkFrame(master=app, fg_color="gray")
agent1_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

#Combobox chọn agent (human hoặc AI)
agent1_combobox = ct.CTkComboBox(master=agent1_frame, values=["AI", "Human"])
agent1_combobox.place(relx=0.5, rely=0.03, anchor=tk.CENTER)

#Combobox chọn các thuật toán
algo1_combobox = ct.CTkComboBox(master=agent1_frame, values=["BFS", "DFS"])
algo1_combobox.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

#Button start
button1_start = ct.CTkButton(master=agent1_frame, text="Start")
button1_start.place(relx=0.5, rely=0.17, anchor=tk.CENTER)

#Button undo
button1_undo = ct.CTkButton(master=agent1_frame, text="Undo")
button1_undo.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

#Canvas để hiện màn hình trò chơi
canvas1 = ct.CTkCanvas(master=agent1_frame,width=720,height = 480)
canvas1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

#Label hiện thời gian giải trò chơi
lb_time1 = ct.CTkLabel(master=agent1_frame,text="Time: 0", text_color="black",width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
lb_time1.place(relx=0.25, rely=0.91)

#Label hiện số bước của thuật toán
lb_step1 = ct.CTkLabel(master=agent1_frame,text="Step: 0", text_color="black",width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
lb_step1.place(relx=0.55, rely=0.91)


#Agent 2
#Tương tự Agent 1
agent2_frame = ct.CTkFrame(master=app, fg_color="gray")
agent2_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

agent2_combobox = ct.CTkComboBox(master=agent2_frame, values=["AI", "Human"])
agent2_combobox.place(relx=0.5, rely=0.03, anchor=tk.CENTER)

algo2_combobox = ct.CTkComboBox(master=agent2_frame, values=["BFS", "DFS"])
algo2_combobox.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button2_start = ct.CTkButton(master=agent2_frame, text="Start")
button2_start.place(relx=0.5, rely=0.17, anchor=tk.CENTER)

button2_undo = ct.CTkButton(master=agent2_frame, text="Undo")
button2_undo.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

canvas2 = ct.CTkCanvas(master=agent2_frame,width=720,height = 480)
canvas2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

lb_time2 = ct.CTkLabel(master=agent2_frame,text="Time: 0", text_color="black",width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
lb_time2.place(relx=0.25, rely=0.91)

lb_step2 = ct.CTkLabel(master=agent2_frame,text="Step: 0", text_color="black",width=120,height=25,fg_color=("white", "gray75"),corner_radius=8)
lb_step2.place(relx=0.55, rely=0.91)

app.mainloop()