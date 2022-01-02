from random import randint

# Encapsulamento:

# Sintaxe:
# Public, Protected, Private. (Outras linguagens).

# Convenção python:
# _(nome_atributo) -> Privado fraco ("Protected")
#   - Pode alterar o atributo com _(nome_atributo) = (novo_valor)
# __(nome_atributo) -> Privado forte ("Private")
#   - Em caso de tentativa de alteração do atributo, o original pode ser acessado com (_(nome_class)__(nome_atributo))

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
        self._nome = nome
        self._preco = preco

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
        # Preciso usar "self._nome", pois "self.nome" representa o setter e getter.
        #   - Logo, se eu usasse "self.nome", acabaria gerando uma recursão infinita.
        #   - "self._nome" -> Atributo.
        #   - "self.nome" -> Getter (.) e Setter (=). (Caso exista as funções getter e setter).
        #       - Caso não exista as funções, "self.nome" representa o atributo.
        return self._nome
    
    # Método setter.
    #   - Chamado sempre que o atributo nome for alterado.
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # getter -> Precisa sempre seguir a sintaxe de:
    #   - Decorador.
    #   - (nome_atributo)(self): return self._(nome_atributo).
    #   - Quando faço isso o atributo se torna "protected", pois agora ele segue a convenção "_(nome_atributo)".
    @property
    def preco(self):
        return self._preco
    
    # getter -> Precisa sempre seguir a sintaxe de:
    #   - Decorador.
    #   - (nome_atributo)(self, (nome_atributo)): self._(nome_atributo)  = (nome_atributo).
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor)
        self._preco = valor

    # Obs: Quando eu crio o getter e setter, toda vez que eu usar "self.(nome_atributo)" e "self.(nome_atributo) =",
    # estou o usando getter e setter, pois por conveção o valor do atributo vai receber o nome "self._(nome_atributo)"
    # ou "self.__(nome_atributo)".

# prod1 = Produto('Bola', 50)
# print(prod1.nome, prod1.preco)
# prod1.desconto(10)
# print(prod1.nome, prod1.preco)
# print(prod1.gera_id())

prod2 = Produto('Camisa', 20)
print(prod2.nome, prod2.preco, prod2.marca)
prod = Produto.produto_marca('Bola', 50, 'NIKE')
print(prod.nome, prod.preco, prod.marca)