#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from config import SCHEMA_MIGRATION, CONF_DAEMON
import os
BASE_DIR = os.path.dirname(__file__)
location = lambda x: os.path.join(BASE_DIR, x)

class Sync(object):

    """
    obj_01 sera sempre o object do tipo ElasticSearch
    """
    def syn_all(self):
        for class_X, class_Y in SCHEMA_MIGRATION.iteritems():
            class_Y = class_Y.split('.')
            class_X = class_X.split('.')
            exec "from models.%s import %s" % (class_Y[0], class_Y[1])
            exec "from models.%s import %s" % (class_X[0], class_X[1])

            if class_X[1] in "ElasticSearch":
                obj_01 = eval(class_X[1])()
                obj_02 = eval(class_Y[1])()
            else:
                obj_01 = eval(class_Y[1])()
                obj_02 = eval(class_X[1])()

            if obj_02.objects.count() != obj_01.count():
                if obj_02.objects.count() > obj_01.count():
                    print "Sync Cassandra to Elasticsearch"
                    for obj in obj_02.objects.all():
                        obj_01.save_cassandra_in_elasticsearch(obj)
                elif obj_02.objects.count() < obj_01.count():
                    print "Elasticsearch To Cassandra"
                    for obj in obj_01.find(size=CONF_DAEMON.get("LIMIT")):
                        obj_02.save_elasticsearch_in_cassandra(obj)
            else:
                print 'Dados Sincronizados'