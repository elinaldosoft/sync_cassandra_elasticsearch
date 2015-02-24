#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from cqlengine.models import Model
from cqlengine import columns
import uuid
from datetime import datetime
from config import CONF_DAEMON

class Base(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4())
    created_at = columns.Integer(default=columns.DateTime().to_database(datetime.now()))

    __abstract__ = True

    def __init__(self, **values):
        self._limit = CONF_DAEMON.get("LIMIT")

        if "created_at" in self.__dict__.keys():
            self.created_at = self.__dict__["created_at"]
        super(Model, self).__init__(**values)

    def save_elasticsearch_in_cassandra(self, obj):
        self.id = obj["_id"]
        for atributo in obj['_source'].keys():
            if atributo:
                if hasattr(self, atributo):
                    setattr(self, atributo, obj["_source"][atributo])
        return self.save()