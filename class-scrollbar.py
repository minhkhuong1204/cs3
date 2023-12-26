from typing import Literal, Optional, Tuple, Union
from typing_extensions import Literal
import customtkinter


class FrameScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master)

        for i in range(1, 1001):
            button = customtkinter.CTkButton(
                master=self, text=f"Button {i}", command=lambda index=i: self.getNumberButton(index))
            button.pack(expand=True, pady=(0, 20))

    def getNumberButton(self, id):
        print(id)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Xin chao TechX")
        self.geometry("600x1400")

        frameScrollBar = FrameScrollBar(self)
        frameScrollBar.pack(expand=True, fill="both")


app = App()
app.mainloop()
