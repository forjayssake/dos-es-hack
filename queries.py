#!/usr/bin/env python
# -*- coding: utf-8 -*-

import elasticsearch
from collections import OrderedDict
import codecs
import json
import datetime
import calendar

#------------------------------------------------------------------------------

def search(es_object, index_name, search):
    res = es_object.search(index=index_name, body=search)
    return res

es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])

now = datetime.datetime.now()
day = calendar.day_name[now.weekday()]
defaultSize = 1

search_object = {"size": defaultSize}

print('QUERY 1 - Boolean search')
print('---------------------------------------------------------------------------------------------------')
search_object = {
        "size": defaultSize,
          "query": {
            "bool": {
              "must": [
                {"match": { "service_name": "NUMSAS"}},
                {"match": { "service_name": "London"}},
              ],
              "must_not": [
                { "match": { "type_name": "local"}}
              ],
            }
        },
        "_source": ["service_name", "uid", "type", "type_name", "postcode"]}


print(search(es, 'service2', json.dumps(search_object)))

print('---------------------------------------------------------------------------------------------------')
print('QUERY 2 - Basic LIKE search')
print('---------------------------------------------------------------------------------------------------')


## opening times query
search_object = {"size": defaultSize, "query": { "match_phrase": {"service_name" : "gp"} }, "_source": ["service_name", "uid"]}
print(search(es, 'service2', json.dumps(search_object)))



