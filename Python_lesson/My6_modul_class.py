import turtle
p1 = turtle.Pen()
p2 = turtle.Pen()

p1.forward (200)
p2.left(90)
p2.forward(150)

class instrumenty_dliy_risovanya:
    def Kto_roditel(self):
        print("Родитель: инструменты для рисования")
    pass
class ruchki (instrumenty_dliy_risovanya):
    pass
class kistochki (instrumenty_dliy_risovanya):
    def __init__(self, _price):
        self.my_price = _price
    def read_price (self):
        print("Моя цена: %s" % self.my_price)
    def write_price(self, _new_price):
        self.my_price = _new_price    
    def kto_ya (self):
        print("я кисточка")
    pass

obj1 = kistochki (205.57)
obj1.kto_ya()
obj1.Kto_roditel()
obj1.read_price()
obj1.write_price(503.73)
obj1.read_price()

obj2 = kistochki (333.15)
obj2.read_price()