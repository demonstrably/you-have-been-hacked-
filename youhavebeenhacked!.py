import tkinter as tk



root = tk.Tk()


root.geometry("400x200")
root.title("bot virus bomba")

label = tk.Label(root, text="you have been hacked", font=('system', 20) )
label.pack(padx=18, pady=18)

def close_window(): 
    root.destroy()

button = tk.Button(root, text = "ok", font=('arial', 16), command=close_window )
button.pack()



root.mainloop() 



