class Player:
    
    def __init__(self, name: str):
        self.name: str = name
        self.level: int = 1
        self.max_hp: int = 100
        self.hp: int = 100
        self.dmg: int = 10
    
    def update(self, hp_change: int):
        self.hp += hp_change
        
    def level_up(self):
        self.max_hp += self.level * 10
        self.hp += self.level * 10
        self.level += 1
        
    def print_stats(self):
        print(f'{self.name}\nLevel: {self.level}\nHealth: {self.hp}/{self.max_hp}\nAtt. power: {self.dmg}')