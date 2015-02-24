#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'elinaldo'
import unittest
from models.posts_elasticsearch import Base
from sync import Sync
from models.posts_elasticsearch import PostsElasticSearch
from models.posts_cassandra import Posts


class ClassDeTestCamelCaseElasticSearch(Base):
    title = str

class TestBaseModel(unittest.TestCase):

    def test_check_reflaction_sync(self):
        Sync().syn_all()

    def setUp(self):
        self.obj_cassandra = Posts()
        self.obj_elasticsearch = PostsElasticSearch()
        self.base_test = ClassDeTestCamelCaseElasticSearch()

    def test_list_all(self):
        for x in self.obj_cassandra.objects.all():
            print x


    def test_save_cassandra(self):
        self.obj_cassandra.title = "Salvando Mas 1 Vez"
        self.obj_cassandra.description = "Iron Maiden"
        self.assertTrue(self.obj_cassandra.save())

    def test_save_elastic_search(self):
        self.obj_elasticsearch.title = "Last Register Insert"
        self.obj_elasticsearch.description = "Dream Theater"
        self.obj_elasticsearch.save()

    def test_padrao_names_class_to_database(self):
        self.assertEqual(self.base_test.class_name, "class_de_test_camel_case")
        self.assertEqual(self.obj_elasticsearch.class_name, "posts")

    def test_check_is_sync(self):
        self.assertEqual(self.obj_cassandra.objects.count(), self.obj_elasticsearch.count(), "Check if estão sincronizados")

    def test_sync_cassandra_to_elasticsearch(self):
        for post in self.obj_cassandra.filter():
            self.obj_elasticsearch.save_cassandra_in_elasticsearch(post)

    def test_sync_elasticsearch_to_cassandra(self):
        for post in self.obj_elasticsearch.find():
            post_cassandra = Posts()
            post_cassandra.save_elasticsearch_in_cassandra(post)

    def test_sync_all(self):
        if self.obj_cassandra.objects.count() != self.obj_elasticsearch.count():
            if self.obj_cassandra.objects.count() > self.obj_elasticsearch.count():
                print "sync cassandra to elasticsearch"
                for post in self.obj_cassandra.all():
                    self.obj_elasticsearch.save_cassandra_in_elasticsearch(post)
            elif self.obj_cassandra.objects.count() < self.obj_elasticsearch.count():
                print "sync elasticsearch to cassandra"
                for post in self.obj_elasticsearch.find():
                    self.obj_cassandra.save_elasticsearch_in_cassandra(post)
        else:
            result = set([x['_id'] for x in self.obj_elasticsearch.find()]) ^ set([str(x.id) for x in self.obj_cassandra.all()])
            if len(result) == 0:
                print 'sync ok!!'

    def test_sync_created_at(self):
        print self.obj_elasticsearch.find(size=1)

if __name__ == '__main__':
    unittest.main()