# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
# -> O pipeline é utilizado principalmente para limpeza de dados e configuração do banco de dados.

class OlxSqlitePipeline(object): # Cada classe representa 1 pipeline diferente.

    # Executado depois que o spider gera um item (yield), recebendo esse item.
    def process_item(self, item, spider):
        # Insere elementos no banco de dados.
        self.conn.execute(
            'insert into cars(titulo, categoria, modelo, marca, ano, tipoVeiculo, cor) values (:titulo, :categoria, :modelo, :marca, :ano, :tipoVeiculo, :cor)',
            item
        )
        # Garante que o item foi salvo no banco de dados.
        # Importante sempre da o commit, pode ser a cada inserção ou antes de fechar o arquivo.
        self.conn.commit()
        return item

    def create_table(self):
        # Verifica se a tabela existe.
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "cars"'
        ) # Retorna um gerador.
        try:
            value = next(result)
        # Se a exceção "StopIteration" for lançada, quer dizer que a tabela não existe, então devo criar.
        except StopIteration as ex:
            # Cria tabela.
            self.conn.execute(
                'create table cars(id integer primary key, titulo text, categoria text, modelo text, marca text, ano text, tipoVeiculo text, cor text)'
            )
    
    # Executado quando o spider abre.
    def open_spider(self, spider):
        # Criando conexão com o banco de dados.
        # Funciona de maneira semelhante a um arquivo:
        #   - Caso o banco exista, ele se conecta ao arquivo.
        #   - Caso o banco não exista, ele cria o arquivo.
        self.conn = sqlite3.connect('db.sqlite3')
        # Criar tabela, se não existir.
        self.create_table()
    
    # Executado quando o spider fecha.
    def close_spider(self, spider):
        # Fecha conexão com o banco.
        self.conn.close()
