Sync CassandraDb to ElasticSearch é uma ferramenta conceito feita para demostrar que é possível sincronizar dados 
entre fontes orientada a documento e outra orientada a colunas.

# Antes de tudo você deve ter instalado:
 * CassandraDB http://cassandra.apache.org/download/ 
 * ElasticSearch http://www.elasticsearch.org/overview/elkdownloads/
 * Python >= 2.7
 
# Install Depêndencias do Python:
 Dentro do Projeto existe o arquivo requirements contento os pacotes que você deve instalar no Python:
 $ pip install -r requirements.txt
 
# Padronização de Classes:
 Por padrão as classes do ElasticSearch deve iniciar sempre neste formado
 NomeDaClassElasticSearch
 