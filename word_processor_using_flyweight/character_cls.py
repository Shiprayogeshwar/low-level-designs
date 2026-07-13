class Character:
    def __init__(self, val, row, col, style):
        self.val = val
        self.row = row
        self.col = col
        self.style = style
    
    def display(self):
        print(f"{self.val} {self.row} {self.col} {self.style}")
