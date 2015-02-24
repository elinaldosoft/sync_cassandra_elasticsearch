#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
from cqlengine import columns
from models.base_cassandra import Base


class Posts(Base):
    description = columns.Text()
    title = columns.Text()