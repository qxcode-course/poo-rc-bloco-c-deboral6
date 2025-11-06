class Cliente:
    def __init__(self, nome: str):
        self._nome = nome

    def getNome(self):
        return self._nome
    
    def __str__(self):
        return f"{self._nome}"
    

class Marker:
    def __init__(self, quantidadeC: int):
        self.caixas: list[Cliente | None] = []
        self.filaEspera: list[Cliente] = []
        for _ in range(quantidadeC):
            self.caixas.append(None)

    def __str__(self):
       caixa = ", ".join([str(cliente) if cliente else "-----" for cliente in self.caixas])
       espera = ", ".join([str(cliente) for cliente in self.filaEspera])
       return f"Caixas: [{caixa}]\nEspera: [{espera}]"
    
    def arrive(self, pessoa: Cliente):
        self.filaEspera.append(pessoa)

    def call(self, index: int):
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
        elif not self.filaEspera:
            print("fail: sem clientes")

        else:
            cliente = self.filaEspera.pop(0)
            self.caixas[index] = cliente

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
        elif self.caixas[index] is None:
            print("fail: caixa vazio")
        else:
            self.caixas[index] = None

def main():
    marker = None

    while True:
        line = input().strip()
        print(f"${line}")
        if not line:
            continue

        partes = line.split()
        comando = partes[0]
        args = partes[1:]

        if comando == "end":
            break

        elif comando == "init":
            if len(args) < 1:
                print("fail: faltam argumentos")
                continue
            qnt = int(args[0])
            marker = Marker(qnt)

        elif comando == "show":
            if marker is None:
                print("fail: inicialize primeiro com 'init'")
            else:
                print(marker)

        elif comando == "arrive":
            if marker is None:
                print("fail: inicialize primeiro com 'init'")
                continue
            if len(args) < 1:
                print("fail: faltam argumentos")
                continue
            nome = args[0]
            marker.arrive(Cliente(nome))

        elif comando == "call":
            if marker is None:
                print("fail: inicialize primeiro com 'init'")
                continue
            if len(args) < 1:
                print("fail: faltam argumentos")
                continue
            try:
                index = int(args[0])
            except ValueError:
                print("fail: argumento invalido")
                continue
            marker.call(index)

        elif comando == "finish":
            if marker is None:
                print("fail: inicialize primeiro com 'init'")
                continue
            if len(args) < 1:
                print("fail: faltam argumentos")
                continue
            try:
                index = int(args[0])
            except ValueError:
                print("fail: argumento invalido")
                continue
            marker.finish(index)

        else:
            print("fail: comando invalido")

if __name__ == "__main__":
    main()
        