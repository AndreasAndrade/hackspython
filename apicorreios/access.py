# coding: utf-8

__author__ = 'Andreas'


from correios import Correios

encomenda = Correios.encomenda('PE129381952BR')

print encomenda.numero

for status in encomenda.status:
    print "Data: %s" % status.data
    print "Local: %s" % status.local
    print "Situacao: %s" % status.situacao
    print "Detalhes: %s" % status.detalhes
    print '-------------------------------'


