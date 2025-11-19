class Criança:
    def __init__(self, nome: str, age: int):
        self.__nome = nome
        self.__age = 0

    def getNome(self):
        return self.__nome
    def getAge(self):
        return self.__age
   
    def __str__(self):
        return f"{self.__nome} {self.__age}"
        
class PulaPula:
    def __init__(self):
        self.fila: list[Criança | None] = []
        self.brinquedo: list[Criança | None] = []

    def chegar(self, criança: Criança):
        self.fila.append(criança)

    def entrar(self):
        if not self.fila:
            print("fail: nao tem ninguem na fila")
            return
        self.brinquedo.append(self.fila.pop(0))

    def sair(self):
        if not self.brinquedo:
            print("fail: nao tem ninguem no pula-pula")
            return
        self.fila.append(self.brinquedo.pop(0))

    def __str__(self):
        fila_str = "[" + ", ".join(str(cria) for cria in self.fila) + "]"
        brinquedo_str = "[" + ", ".join(str(cria) for cria in self.brinquedo)+ "]"
        return f"{fila_str} {brinquedo_str}"
    
def main():
    pulapula = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            pulapula.chegar(Crianca(nome, idade))

        elif args[0] == "enter":
            pulapula.entrar()

        elif args[0] == "leave":
            pulapula.sair()

        elif args[0] == "remove":
            nome = args[1]
            pulapula.remover(nome)

            


    
    
        






        


        