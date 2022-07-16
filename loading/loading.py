import json
import logging

import data_classes

class Loading:
    def __init__(self):
        self.entities = []
        self.rooms = []
        self.obj = self.load_game_data()

        self.init_entities()
        self.init_rooms()

    def load_game_data(self):
        with open("gamedata.json") as game_file:
            game_data = game_file.read()

        return json.loads(game_data)

    def init_rooms(self):
        for room in self.obj['rooms']:
            temp_room = data_classes.Room(room['name'],room['description'],room['connections'],room['entities'])
            self.rooms.append(temp_room)
        
        self.get_room_index()
        self.load_entities()

    # Links rooms
    def get_room_index(self):
        for room in self.rooms:
            if room.connections:
                # Replace room name in connections with index of room object
                room.connections = [room_index[0] for room_name in room.connections 
                                    for room_index in enumerate(self.rooms)
                                    if room_name == self.rooms[room_index[0]].name]
        logging.info(self.rooms)
               

    def init_entities(self):
        for entity in self.obj['entities']:
            temp_entitie = data_classes.Entity(entity['name'])
            self.entities.append(temp_entitie)
        
        for character in self.obj['characters']:
            temp_character = data_classes.Character(character['name'], character['helth'], 
                character['agility'], character['presence'], character['strength'], character['toughness'])
            self.entities.append(temp_character)

    def load_entities(self):
        for room in self.rooms:
            if room.entities:
                # Replace entity name in entities list with an object
                room.entities = [entity_object for entity_name in room.entities 
                                for entity_object in self.entities
                                if entity_name == entity_object.name]
        logging.info(self.entities)
