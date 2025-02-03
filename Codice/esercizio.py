class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi(self,dx,dy):
        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):
        return (self.x**2 + self.y**2)**0.5 
    
    
p1 = Punto (3,4)
print("x: ",p1.x, "y: " ,p1.y)

print("distanza: ", p1.distanza_da_origine())

p2 = Punto (3,4)
p2.muovi(1,1)
print("x: ",p2.x,"y: " ,p2.y)
print("distanza: ",p2.distanza_da_origine())

