Sync CassandraDb to ElasticSearch é uma ferramenta conceito feita para demostrar que é possível sincronizar dados 
entre fontes orientada a documento e outra orientada a colunas.

# Antes de tudo você deve ter instalado:
 * CassandraDB http://cassandra.apache.org/download/ 
 * ElasticSearch http://www.elasticsearch.org/overview/elkdownloads/
 * Python >= 2.7
 
# Instale as Depêndencias do Python:
 Dentro do Projeto existe o arquivo requirements contento os pacotes que você deve instalar no Python:
 
 ```
 $ pip install -r requirements.txt
 ```
 
# Padronização de Classes:
 Por padrão as classes do ElasticSearch deve iniciar sempre neste formado.
 
### Padrão ElasticSearch Class
 
 ```
 NomeDaClassElasticSearch
 Ex: PostElasticSearch
 ```
 Todas as classes do Tipo ElasticSearch deve herdar da class Base:
 
 ```
    from cqlengine import columns
    from models.base_elasticsearch import Base
    
    class TestElasticSearch(Base):
        atributo_a = columns.Text()
        atributo_b = columns.Integer()
        atributo_c = columns.Float()
        
 ```
 Por padrão o nome da coleção no ElasticSearch vai ficar **test** sendo que você tem a opção de utilizar o paramentro
  __ table__ para alterar o nome de onde deve ser salvo os dados:
 
 ```
 from cqlengine import columns
    from models.base_elasticsearch import Base
    
    class TestElasticSearch(Base):
        atributo_a = columns.Text()
        atributo_b = columns.Integer()
        atributo_c = columns.Float()
        
        __table__ = 'logs'
 ```
 
 Se você observar bem estamos utilizando o pacote **cqlengine** para fazer o mapeamento dos fields do ElasticSearch 
 sendo que este pacote é um ORM para o cassandra. Pude observar que poderia desfrutar desse recurso de mapeamento 
 tanto para o cassandra e elasticseach