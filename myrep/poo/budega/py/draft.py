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
       caixa = ", ".join([str(cliente) if cliente else "----" for cliente in self.caixas])
       espera = ", ".join([str(cliente) for cliente in self.filaEspera])
       return f"Caixas: {caixa}\n Espera: {espera}"
    
    def chegar(self, pessoa: Cliente):
        espera.append(pessoa)

        