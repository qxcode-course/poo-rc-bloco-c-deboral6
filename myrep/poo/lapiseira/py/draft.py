class Grafite:
    def __init__(self, calibre: float, dureza: str, tam: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.tam = tam

    def setTam(self, valor):
        self.setTam = valor
    def getCalibre(self):
        return self.__calibre
    def getDureza(self):
        return self.__dureza
    def getTam(self):
        return self.tam
    
    def __str__(self):
        return f"{self.__calibre}: {self.__dureza}: {self.tam}"
        
class Lapiseira:
    def __init__(self, calibre: float, bico: float):
        self.__calibre: float
        self.bico = float
        self.tambor: list[Grafite | None] = []

    def insert(self, graf: Grafite):
        if graf.getCalibre() == self.__calibre:
            self.tambor.append(graf)
        else:
            print("fail: grafite incompativel")

    def puxarGrafite(self):
        if self.__bico is not None:
            print("fail: já existe grafite no bico")
            return
        if not self.tambor:
            print("fail: o tambor está vazio")
        self.__bico = self.tambor.pop(0)

    def removerGrafite(self):
        if self.bico is None:
            print("fail: não há grafite no bico")
        self.bico = None

    def escrever(self):
        if self.__bico is None:
            print("fail: nao existe grafite no bico")
            return
        gasto = self.bico.gastoFolha()
        tamanho = self.bico.getTam() 

        if tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        if tamanho - gasto < 10:
            print("fail: folha incompleta")
            self.__bico = None
            return
        
        self.bico.setTam( tamanho - gasto)

        if self.__bico.getTam() == 10:
            self.__bico = None

        




        

        
    


    
    


        


        
        