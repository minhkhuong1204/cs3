import customtkinter

root = customtkinter.CTk()

root.title("tech X")

root.geometry("600x400")
frameTop = customtkinter.CTkFrame(master=root)

frameTop.pack(expand=True, fill="both")

frameBot = customtkinter.CTkFrame(master=root)

frameBot.pack(expand=True, fill="both")

frameChild1 = customtkinter.CTkFrame(master=frameTop, fg_color="blue")

frameChild1.pack(side="left", fill="both", expand=True)

frameChild2 = customtkinter.CTkFrame(master=frameTop, fg_color="white")

frameChild2.pack(side="right", fill="both", expand=True)

frameChild3 = customtkinter.CTkFrame(master=frameBot, fg_color="red")

frameChild3.pack(side="left", fill="both", expand=True)

frameChild4 = customtkinter.CTkFrame(master=frameBot, fg_color="black")

frameChild4.pack(side="right", fill="both", expand=True)


root.resizable(width=True, height=False)

root.mainloop()
