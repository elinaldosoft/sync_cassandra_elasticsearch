#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
import uuid
import re
from config import es
from datetime import datetime
from cqlengine import columns

class Base(object):
    id = columns.UUID(primary_key=True, default=uuid.uuid4())

    __abstract__ = True
    __table__ = None

    def __init__(self):
        if not "created_at" in self.__dict__.keys():
            self.__dict__["created_at"] = columns.DateTime().to_database(datetime.now())

    @property
    def class_name(self):
        if self.__table__:
            return self.__table__
        else:
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', self.__class__.__name__)
            s1 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
            return "_".join(s1.split("_")[:-2])

    def save(self):
        if "id" in self.__dict__.keys():
            id_uuid = self.__dict__["id"]
            del self.__dict__["id"]
            return es.index(index="id", doc_type=self.class_name, id=id_uuid, body=self.__dict__)
        else:
             return es.index(index="id", doc_type=self.class_name, id=uuid.uuid4(), body=self.__dict__)

    def save_cassandra_in_elasticsearch(self, obj):
        for atributo in obj.keys():
            if hasattr(self, atributo):
                setattr(self, atributo, getattr(obj, atributo))
        return self.save()

    def count(self):
        return es.count(index="id", doc_type=self.class_name)['count']

    def find(self, size=100):
        return es.search(index="id", doc_type=self.class_name, size=size, sort={'created_at':'desc'})['hits']['hits']