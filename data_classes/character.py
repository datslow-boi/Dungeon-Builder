from dataclasses import dataclass
from .entity import Entity

@dataclass
class Character(Entity):
    helth: int
    agility : int
    presence : int
    strength : int
    toughness : int

    def info(self):
        return f"{self.name} {self.helth} {self.agility} {self.presence} {self.nastrengthme} {self.toughness}"