#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from elasticsearch import Elasticsearch

CASSANDRA = {
    'IP': ['127.0.0.1'],
    'DB': u'cassandra_db',
}

es = Elasticsearch(
    ['localhost'],
    port=9200,
)

"""
TIME - Você dever definir o tempo em segundos para determinar de quanto em quanto tempo haverá
uma sincronização de dados entre o Cassandra e o ElasticSearch.
"""
CONF_DAEMON = {
    'TIME': 10,
    'LIMIT': 100,
}

SCHEMA_MIGRATION = {
    'posts_cassandra.Posts': 'posts_elasticsearch.PostsElasticSearch',
}