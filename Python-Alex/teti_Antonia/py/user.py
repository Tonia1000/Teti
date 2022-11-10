class Ususario:
    def __init__(self): # __init__ e o nome para o construtor
        self.id_usuario = 0
        self.name = ""
        self.password = ""
    
    def validate(self):
        if self.password=="123" and self.name=="Ze": # and self.id_usuario == 10:
            return True

