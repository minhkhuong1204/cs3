import customtkinter

root = customtkinter.CTk()

root.title("tech X")
root.geometry("600x400")
root.columnconfigure((0, 1), weight=1)

# master phụ thuộc vào ai
frame = customtkinter.CTkFrame(master=root, fg_color="yellow")

frame.grid(column=0, row=0, sticky="nswe")

frame1 = customtkinter.CTkFrame(root, fg_color="red")
frame1.grid(column=1, row=0, sticky="nswe")

frame2 = customtkinter.CTkFrame(master=root, fg_color="blue")

frame2.grid(column=0, row=1, sticky="nswe")

frame3 = customtkinter.CTkFrame(root, fg_color="gray")
frame3.grid(column=1, row=1, sticky="nswe")


root.resizable(width=True, height=False)

root.mainloop()
