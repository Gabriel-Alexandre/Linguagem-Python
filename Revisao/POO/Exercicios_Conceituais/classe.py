from random import randint

class Produto:
    # Atributo de classe.
    #   - Todas as classes vão ter o mesmo atributo.
    marca = 'MARCA'

    # Método construtor.
    #   - Utilizado para iniciar os atributos de instância.
    # self -> referência a instância (objeto).
    def __init__(self, nome, preco):
        # Atributos de instância.
        #   - Cada instância vai ter um atributo diferente.
        #   - Pode ser criado fora da classe.
        self.nome = nome
        self.preco = preco

    # Método de classe. 
    #   - Disponível apenas para a classe.
    #   - Utiliza a classe.
    # cls -> referência a classe.
    @classmethod
    def produto_marca(cls, nome, preco, marca):
        cls.marca = marca
        return cls(nome, preco)
    
    # Método estático.
    #   - Disponível para classe e para instância.
    #   - Não utiliza nem a classe, nem a instância.
    @staticmethod
    def gera_id():
        return randint(1000, 1999)

    # Método de instância.
    #   - Disponível para instância.
    #   - Utiliza a instância.
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
    
    # Método getter.
    #   - Chamado sempre que o atributo nome for solicitado.
    @property
    def nome(self):
        return self._nome
    
    # Método setter.
    #   - Chamado sempre que o atributo nome for alterado.
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor)
        self._preco = valor

# prod1 = Produto('Bola', 50)
# print(prod1.nome, prod1.preco)
# prod1.desconto(10)
# print(prod1.nome, prod1.preco)
# print(prod1.gera_id())

prod2 = Produto('Camisa', 20)
print(prod2.nome, prod2.preco, prod2.marca)
prod = Produto.produto_marca('Bola', 50, 'NIKE')
print(prod.nome, prod.preco, prod.marca)