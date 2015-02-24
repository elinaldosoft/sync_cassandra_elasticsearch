#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from base_elasticsearch import Base
from cqlengine import columns

class PostsElasticSearch(Base):
    title = columns.Text()
    description = columns.Text()