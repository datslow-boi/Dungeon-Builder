from dataclasses import dataclass


@dataclass
class Room:
    name : str
    description : str
    connections : list
    entities : list

    def info(self):
        entitie_list = []
        for i in range(len(self.entities)):
            entitie_list.append(self.entities[i].name)
        
        return f"{self.name}\n{self.description}\n{self.connections}\n{entitie_list}"