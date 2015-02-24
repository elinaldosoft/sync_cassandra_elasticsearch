#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from elasticsearch import Elasticsearch

"""
http://datastax.github.io/python-driver/api/cassandra/cluster.html
"""
CASSANDRA = {
    'IP': ['127.0.0.1'],
    'DB': u'cassandra_db',
}

"""
https://elasticsearch-py.readthedocs.org/en/master/api.html#global-options
"""
es = Elasticsearch(
    ['localhost'],
    port=9200,
)

"""
TIME - Você dever definir o tempo em segundos para determinar de quanto em quanto tempo haverá
uma sincronização de dados entre o Cassandra e o ElasticSearch.
LIMIT - limita o número de registro que será sincronizado de cada vez
PID_PATH - Caminho onde vai ficar o arquivo com o número do processo em daemon
"""
CONF_DAEMON = {
    'TIME': 10,
    'LIMIT': 100,
    'PID_PATH': '/tmp/sync_daemon.pid'
}

"""
SCHEMA_MIGRATION - É onde você define quais Classes serão sincronizados entre se.
"""
SCHEMA_MIGRATION = {
    'posts_cassandra.Posts': 'posts_elasticsearch.PostsElasticSearch',
}