'''
import requests, json, os
from elasticsearch import Elasticsearch

directory = 'c:/users/mabe13/elasticimport/'

res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

i = 1

for filename in os.listdir(directory):
	if filename.endswith(".json"):
		f = open(filename)
		docket_content = f.read()
		es.index(index='service', doc_type='json', id=i, body=json.loads(docket_content))
		i = i + 1
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import elasticsearch
import requests
from collections import OrderedDict
import codecs
import json
import psycopg2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = None
try:
  conn = psycopg2.connect(host="localhost",database="pathwaysdos_dev", user="postgres", password="postgres")

  cur = conn.cursor()
  #print('PostgresSQL database version:')
  #cur.execute('SELECT version()')

  #db_version = cur.fetchone()
  #print(db_version)

  print("Creating or replacing view for extract")
  #psqlFile = open("-.sql")
  psqlFile = codecs.open("-.sql", "r", "utf-8")
  psql = psqlFile.read()
  print(psql);
  psqlFile.close()
  cur.execute(psql)

  print("Select services from view")
  cur.execute("SELECT elastic_bulk_service FROM pathwaysdos.elastic_search_2")
  services = cur.fetchall()
  print("exported services count:"+str(len(services)))

  servicesStr = []
  for i in range(len(services)):
      servicesStr.append(''.join(services[i]))


  print("Import into Elasticsearch")
  es=elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
  res=es.bulk(body=servicesStr, ignore=400, index="services", doc_type="service",request_timeout=30)
  print(json.dumps(res, indent=3, separators=(',', ': ')))

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed')
