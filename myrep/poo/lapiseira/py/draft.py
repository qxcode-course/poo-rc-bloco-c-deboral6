class Grafite:
    def __init__(self, calibre: float, dureza: str, tam: int):
        self._calibre = calibre
        self._dureza = dureza
        self._tam = tam

    def getCalibre(self):
        return self._calibre
class Lapiseira:
    def __init__(self, calibre: float, bico: int):
        self._calibre = calibre
        self.bico = bico
        self.grafite = None

    def insert(self, graf: Grafite):
        if graf.getCalibre() == self._calibre:
            self._grafite = graf

        elif graf.getCalibre() == self._calibre:
            print("já existe grafite")
        else: 
            print("fail: grafite incompativel")

        


        
        