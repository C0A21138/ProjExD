import tkinter as tk




if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    
    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")

    tori = tk.PhotoImage(file="fig0/.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    canvas.pack()
    root.mainloop()
