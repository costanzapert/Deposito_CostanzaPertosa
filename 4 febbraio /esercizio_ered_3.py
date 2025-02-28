class Ram:
    def __init__(self, memoria):
        self.memoria = memoria
    
    def stato_memoria(self):
        return "Memoria disponibile"
    
class CPU: 
    def __init__(self, velocita):
        self.velocita = velocita
    
    def descrizione_velocita(self):
        return "La velocita è di", self.velocita
    
class Computer(Ram,CPU): 
    def __init__(self,memoria,velocita):
        Ram.__init__(self, memoria)
        CPU.__init__(self, velocita)
    

    def stampa_descrizione_completa(self):
        x= super().stato_memoria()
        print(self.descrizione_velocita())
        print( x )
        #print("Lo stato della memoria è:", self.stato_memoria(),"mentre", self.descrizione_velocità())

ram1= Ram(12)
cpu1= CPU(30)
comp1 = Computer(ram1,30)
comp1.stampa_descrizione_completa()
print(cpu1.descrizione_velocita())

    
        