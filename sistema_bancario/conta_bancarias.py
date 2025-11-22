from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self.nome = nome; self.idade = idade

class Cliente(Pessoa):
    @abstractmethod
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

class Conta(Cliente, ABC):
    @abstractmethod
    def __init__(self, nome, idade, agencia, conta, saldo=None):
        super().__init__(nome, idade)
        self.agencia = agencia; self._saldo = saldo; self.conta = conta

    def sacar(self, valor_saque=0):
        self._valor_saque = valor_saque
        if self._valor_saque > self._saldo:
            print("Valor de saque acima do saldo")
            return self._saldo
        print("Saque realizado com sucesso")
        self._saldo -= self._valor_saque; return self._saldo

class ContaCorrente(Conta):
    def __init__(self, nome, idade, agencia, conta, saldo=0):
        super().__init__(nome, idade, agencia, conta, saldo)
        print()
        try: 
            self._saldo = float(self._saldo) ; self.__saldo_extra = 200
            if self._saldo is None or self._saldo <= 0:
                self._saldo += self.__saldo_extra ; print(f"{self.nome}, Sua conta foi criada com Sucesso!") ; print("Você recebeu um saldo extra de R$ 200,00")
            return
        except (ValueError, TypeError) as erro: 
            print("Ocorreu um erro: ", erro)
        
    def depositar(self, valor_deposito):
        print("Saldo extra foi retirado")
        self._saldo -= self.__saldo_extra; self._saldo += valor_deposito
        return self._saldo
    
    def meu_saldo(self):
        print(self._saldo)

    def __repr__(self): return ContaCorrente.__name__

    def to_dict(self):
        return{
            "nome": self.nome,
            "idade": self.idade,
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self._saldo,
            "tipo_conta": __class__.__name__
    }
    

class ContaPoupanca(Conta):
    def __init__(self, nome, idade, agencia, conta, saldo=0):
        super().__init__(nome, idade, agencia, conta, saldo)
        try: 
            self._saldo = float(self._saldo)
            return
        except (ValueError, TypeError) as erro: 
            print(f"{self.nome}: Conta não criada: ", erro)

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito; return self._saldo

    def meu_saldo(self):
        print(self._saldo)

    def __repr__(self): return "Conta Poupança"

    def to_dict(self):
        return{
            "nome": self.nome,
            "idade": self.idade,
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self._saldo,
            "tipo_conta": __class__.__name__
    }

class Banco(Conta, Cliente):
    @abstractmethod
    def __init__(self, nome, idade, agencia, conta, saldo=None):
        super().__init__(nome, idade, agencia, conta, saldo)


def validar_idade(idade):
    return False if idade < 18 else True