# coding: utf-8

import urllib2
import json
import pprint

# url = 'https://graph.facebook.com/andreas.andrade.1'
token='CAACEdEose0cBALq2jzk6JG0oYN5ssLlAzaJFnBLV1JZCrkQVRU1zguQUMjWf2li9r0JS56g4lbRNQ8ZCZBU3AwD1wFGolDXBynPkasjZAcRecoi4hzf5xtrqUFQjN1BlEfPiVy2xDuPSGgRT9iOZB832gxDf4wu8H4JB2WglAayHa9RWzVUcCjouQrS310ZCCCgkkXKK3yyTQDnZBOrTK5e'
url = 'https://graph.facebook.com/800348820003428/picture?type=large'
resp = urllib2.urlopen(url, data={'access_token': 'CAACEdEose0cBALq2jzk6JG0oYN5ssLlAzaJFnBLV1JZCrkQVRU1zguQUMjWf2li9r0JS56g4lbRNQ8ZCZBU3AwD1wFGolDXBynPkasjZAcRecoi4hzf5xtrqUFQjN1BlEfPiVy2xDuPSGgRT9iOZB832gxDf4wu8H4JB2WglAayHa9RWzVUcCjouQrS310ZCCCgkkXKK3yyTQDnZBOrTK5e'}).read()
data = json.loads(resp.decode('utf-8'))

pprint (data)