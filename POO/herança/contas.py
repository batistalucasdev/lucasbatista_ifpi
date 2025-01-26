class ContaCorrente:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo

    def __str__(self):
        return f"ContaCorrente [Número: {self.numero}, Titular: {self.titular}, Saldo: {self._saldo}]"

    def creditar(self, valor):
        if valor > 0:
            self._saldo += valor

    def debitar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self._saldo:
            self.debitar(valor)
            conta_destino.creditar(valor)

class ContaPoupanca(ContaCorrente):
    def renderJuros(self, taxa_juros):
        if taxa_juros > 0:
            self._saldo += self._saldo * (taxa_juros / 100)

class ContaImposto(ContaCorrente):
    def __init__(self, numero, titular, saldo=0, percentual_imposto=0):
        super().__init__(numero, titular, saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_Imposto(self):
        if self.percentual_imposto > 0:
            imposto = self._saldo * (self.percentual_imposto / 100)
            self._saldo -= imposto

    def __str__(self):
        return (f"ContaImposto [Número: {self.numero}, Titular: {self.titular}, Saldo: {self._saldo}, "
                f"Percentual Imposto: {self.percentual_imposto}%]")

def main():
    conta1 = ContaCorrente("001", "João", 1000)
    conta2 = ContaCorrente("002", "Maria", 500)
    poupanca = ContaPoupanca("003", "Ana", 2000)
    imposto = ContaImposto("004", "Carlos", 3000, 5)

    print(conta1)
    conta1.creditar(200)
    print(conta1)
    conta1.debitar(500)
    print(conta1)
    print("")

    conta1.transferir(200, conta2)
    print(conta1)
    print(conta2)
    print("")
    
    print(poupanca)
    poupanca.renderJuros(2)
    print(poupanca)
    print("")

    print(imposto)
    imposto.calcula_Imposto()
    print(imposto)
    print("")

if __name__ == "__main__":
    main()
