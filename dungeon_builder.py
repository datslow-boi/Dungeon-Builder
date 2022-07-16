import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog

import pages
import loading


class Dungeon_builder:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("Dungeon Builder")

        self.rooms = loading.loader.rooms
        self.entities = loading.loader.entities

        
        page = pages.Room_graphics(self.root)
        page.update_data(self.rooms, self.entities, 0)


        self.root.mainloop()




if __name__=='__main__':
    program = Dungeon_builder()



