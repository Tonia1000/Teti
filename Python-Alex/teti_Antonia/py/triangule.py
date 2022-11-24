import math

class Triangule:
#construtor
    def __init__(self, a_lado, b_lado, c_lado):
        self.a_lado = a_lado
        self.b_lado = b_lado
        self.c_lado = c_lado
    
    def get_perimetro(self)-> int:
        return self.a_lado+self.b_lado+self.c_lado

    def get_lado_maior(self)-> int:
        return max(self.a_lado, self.b_lado, self.c_lado)

    def get_area(self)-> float:
        perimetro = int(self.get_perimetro()/2)
        p = perimetro
        a = self.a_lado
        b = self.b_lado
        c = self.c_lado
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return float(f"{area:2f}")