from abc import ABC, abstractmethod

d = [{'nome': 'Gabriel', 'idade': 20}]

dados_banco = [
    {
        'nome_cliente': 'Gabriel',
        'agencia': '10044',
        'numero_conta': '200044'
    }, 
    {
        'nome_cliente': 'Emanuel',
        'agencia': '10045',
        'numero_conta': '200045'
    },
    {
        'nome_cliente': 'Alex',
        'agencia': '10046',
        'numero_conta': '200046'
    },
    {
        'nome_cliente': 'Anderson',
        'agencia': '10046',
        'numero_conta': '200046'
    }
]

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo, auteticado=False):
        if not isinstance(agencia, str):
            raise ValueError('Agência precisa ser uma string!')
        if not isinstance(numero_conta, str):
            raise ValueError('Número conta precisa ser uma string!')
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._autenticado = auteticado

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def autenticado(self):
        return self._autenticado

    @autenticado.setter
    def autenticado(self, valor):
        self._autenticado = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor não reconhecido! Digite um valor inteiro ou de ponto flutuante!')

        if not self.autenticado:
            raise ValueError('Cliente não autenticado')
        self._saldo += valor

    @abstractmethod
    def sacar(self):
        pass

class ContaCorrete(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        super().__init__(agencia, numero_conta, saldo)

        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor não reconhecido! Digite um valor inteiro ou de ponto flutuante!')

        if not self.autenticado:
            raise ValueError('Cliente não autenticado')

        if valor > (self.saldo + self.limite):
            print(f'saldo insuficiente!')

        self._saldo -= valor



class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print('Valor não reconhecido! Digite um valor inteiro ou de ponto flutuante!')

        if not self.autenticado:
            raise ValueError('Cliente não autenticado')

        if valor > self.saldo:
            print(f'saldo insuficiente!')

        self._saldo -= valor


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)

        self._conta = conta

    @property
    def conta(self):
        return self._conta

    def detalhes_conta(self):
        print(f'Agência: {self.conta.agencia}')
        print(f'Número conta: {self.conta.numero_conta}')
        print(f'Saldo: {self.conta.saldo}')
        if isinstance(self.conta, ContaCorrete):
            print(f'Limite: {self.conta.limite}')
        

class Banco():
    def __init__(self, conta, cliente):
        self._conta = conta
        self._cliente = cliente
        if self.autenticar():
            self.conta.autenticado = True
        else:
            self.conta.autenticado = False

    @property
    def conta(self):
        return self._conta
    
    @property
    def cliente(self):
        return self._cliente

    def autenticar(self):
        for dado in dados_banco:
            if dado['nome_cliente'] == self.cliente.nome and \
            dado['agencia'] == self.conta.agencia and \
            dado['numero_conta'] == self.conta.numero_conta:
                return True

        return False
        


cp = ContaPoupanca('1000', '002020', 400) # Não autenticado
cna = Cliente('Teste', 19, cp) # Não autenticado
cc = ContaCorrete('10044', '200044', 500, 100) # Autenticado
ca = Cliente('Gabriel', 19, cc) # Autenticado

banco = Banco(cc, ca)
banco.conta.depositar(100)
banco.conta.sacar(50)
banco.cliente.detalhes_conta()

# Tem pontos de melhoria, mas serviu para treinar bem os assuntos:

# - Encapsulamento.
# - Agregação.
# - Herança.
# - Polimorfismo.
# - Classes abstratas.
# - Entre outros assuntos.