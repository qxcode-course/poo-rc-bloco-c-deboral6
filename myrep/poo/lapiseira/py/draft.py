class Grafite:
    def __init__(self, calibre: float, dureza: str, tam: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.tam = tam

    def getCalibre(self):
        return self.__calibre
    
    def getTam(self):
        return self.tam
    
    def gastar(self, valor):
        self.tam -= valor
        if self.tam < 0:
            self.tam = 0
    def usageParsheet(self):
        return 4
    def __str__(self):
        return f"{self.__calibre}: {self.__dureza}: {self.tam}"
        
class Lapiseira:
    def __init__(self, calibre: float, bico: float):
        self.__calibre: float
        self.bico = float
        self.tambor: list[Grafite | None] = []

    def getCalibre(self) -> float:
        return self.__calibre
    
    def getBico(self) -> Grafite | None:
        return self.bico
    
    def getTambor(self) -> list[Grafite]:
        return self.tambor

    def insert(self, graf: Grafite):
        if graf.getCalibre() == self.__calibre:
            self.tambor.append(graf)
        else:
            print("fail: grafite incompativel")

    def puxarGrafite(self):
        if self.__bico is not None:
            print("fail: ja existe grafite no bico")

        if len(self.tambor) == 0:
            print("fail: tambor vazio")
            return
        self.__bico = self.tambor.pop(0)

    def removerGrafite(self):
        if self.bico is None:
            print("fail: não existe grafite no bico")
        self.bico = None

    def escrever(self):
        if self.__bico is None:
            print("fail: nao existe grafite no bico")
            return
        
        if self.__bico.getTam() <= 10:
            print("fail: tamanho insuficiente")
            return
        gasto = self.__bico.usageParsheet()

        if self.__bico.getTam() - gasto < 10:
            print("fail: folha incompleta")
            self.__bico.gastar(self.__bico.getTam() - 10)
            return
        
        self.__bico.gastar(gasto)

    def __str__(self):
        return f"calibre{self.__calibre}"
    
def main():
    lapiseira = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
            continue
        elif args[0] == "show":
            calibre = lapiseira.getCalibre()
            bico = lapiseira.getBico()
            tambor = lapiseira.getTambor()

            bico_str = str(bico) if bico is not None else "[]"
            tambor_str = "<" + "".join(str(g) for g in tambor) + ">" if len(tambor) else "<>"

            print(f"calibre: {calibre}, bico: {bico_str}, tambor: {tambor_str}")
        
        elif args[0] == "insert":
                calibre = float(args[1])
                dureza = args[2]
                tam = int(args[3])
                graf = Grafite(dureza, calibre, tam)
                lapiseira.insert(graf)

        elif args[0] == "pull":
            lapiseira.puxarGrafite()

        elif args[0] == "remove":
            lapiseira.removerGrafite()

        elif args[0] == "white":
            lapiseira.escrever()
        elif args[0] == "show":
            print(lapiseira)
main()





        

        




        

        
    


    
    


        


        
        