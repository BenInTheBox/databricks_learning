from .player import Player

class Tank(Player):
    
    def __init__(self, name: str):
        super().__init__(name)
        
    def level_up(self):
        self.max_hp += self.level * 15
        self.hp += self.level * 15
        self.level += 1 