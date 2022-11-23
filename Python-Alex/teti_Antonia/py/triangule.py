
class Triangule

#construtor

    def get_perimetro(self)-> int:
        return self.a_lado+self.b_lado+self.c_lado

    def get_lado-maior(self)-> int:
        return max(self.a_lado, self.b_lado, self.c_lado)

    def get_area(self)-> float:
        perimetro = int(self.get_perimetro()/2)
        p = perimetro
        a = self.a_lado
        b = self.b_lado
        c = self.c_lado
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return float(f"{area:2f}")