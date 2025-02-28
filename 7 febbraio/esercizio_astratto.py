from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro")

class Pesce(Animale):
    def muovi(self):
        print("Nuoto")

#a1=Animale()
#a1.muovi()

c1= Cane()
c1.muovi()

p1= Pesce()
p1.muovi()
