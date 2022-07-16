from html import entities
import tkinter as tk


class Room_graphics:
    def __init__(self, root) -> None:
        self.root = root

        self.rooms = []
        self.entities = []
        self.room = 0

        self.room_feilds()

    def room_feilds(self):
        self.left_frame, self.right_frame, self.feild_frame, self.list_frame, self.list_column = self.init_frames()
        
        self.name_widgets(self.feild_frame)
        self.description_widgets(self.feild_frame)
        self.connection_widgets(self.list_frame)
        self.entities_widgets(self.list_frame)
        self.side_panel(self.list_column)

        self.draw_frames(self.left_frame, self.right_frame, self.feild_frame, self.list_frame, self.list_column)

    def draw_frames(self, left_frame, right_frame, feild_frame, list_frame, list_column):
        list_column.pack()
        feild_frame.pack()
        list_frame.pack()
        left_frame.grid(row=0,column=0)
        right_frame.grid(row=0,column=1)

    def init_frames(self):
        left_frame = tk.Frame(self.root)
        right_frame = tk.Frame(self.root)
        feild_frame = tk.Frame(right_frame)
        list_frame = tk.Frame(right_frame)
        list_column = tk.Frame(left_frame)
        return left_frame,right_frame,feild_frame,list_frame,list_column

    def side_panel(self, list_column):
        side = tk.Listbox(list_column)
        side.pack(fill='y')
        for i in enumerate(self.rooms):
            self.item_box(side, self.rooms[i[0]].name)

    def entities_widgets(self, list_frame):
        label = tk.Label(list_frame, text="Entities", font=("Arial", 18))
        label.grid(padx=20, pady=1, row=0, column=1)
        entity_box = tk.Listbox(list_frame)
        entity_box.grid(row=1, column=1)
        if self.entities:
            for i in enumerate(self.rooms[self.room].entities):
                self.item_box(entity_box, self.rooms[self.room].entities[i[0]].name)
        add = tk.Button(list_frame, text="Add Entity", font=("Arial", 9))
        add.grid(padx=20, pady=1, row=2, column=1)

    def item_box(self, parent, text):
        label = tk.Button(parent, text=text, font=("Arial", 9))
        label.pack(padx=20, pady=1)

    def connection_widgets(self, list_frame):
        label = tk.Label(list_frame, text="Connections", font=("Arial", 18))
        label.grid(padx=20, pady=1, row=0, column=0)
        connections = tk.Listbox(list_frame)
        connections.grid(row=1,column=0)
        if self.rooms:
            for i in self.rooms[self.room].connections:
                self.item_box(connections, f"{self.rooms[self.room].connections}")

        add = tk.Button(list_frame, text="Add connection", font=("Arial", 9))
        add.grid(padx=20, pady=1, row=2, column=0)

    def description_widgets(self, feild_frame):
        label = tk.Label(feild_frame, text="Description", font=("Arial", 18))
        label.pack(padx=20, pady=1)

        textbox = tk.Text(feild_frame, font=("Arial", 12), height=3)
        if self.rooms:
            textbox.insert(tk.INSERT, self.rooms[self.room].description)
        textbox.pack(padx=20, pady=10)

    def name_widgets(self, feild_frame):
        label = tk.Label(feild_frame, text="Name", font=("Arial", 18))
        label.pack(padx=20, pady=1)

        textbox = tk.Entry(feild_frame, font=("Arial", 12))
        if self.rooms:
            textbox.insert(tk.INSERT, self.rooms[self.room].name)
        textbox.pack(padx=20, pady=10)

    def update_data(self, rooms, entities, room):
        self.rooms = rooms
        self.entities = entities
        self.room = room
        self.left_frame.destroy()
        self.right_frame.destroy()
        self.room_feilds()
