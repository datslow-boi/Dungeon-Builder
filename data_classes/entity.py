from dataclasses import dataclass


@dataclass
class Entity:
    name : str

    def info(self):
        return f"{self.name}"

